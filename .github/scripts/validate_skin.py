#!/usr/bin/env python3
"""Reference-integrity checks for the OSMC skin.

Kodi fails these silently: a missing <include> logs a warning at most, an unknown
$VAR[] logs nothing at all, and a duplicate include name is dropped without a
word (CGUIIncludes::LoadIncludes uses try_emplace, so the first definition wins).
None of them are visible by loading the skin and looking at it, which is why they
survive for years.

Blocking checks — these are the skin's own bugs, and a pull request should not
land while one is outstanding:

  1. include/variable/expression names referenced but never defined
  2. names defined more than once in the same file
  3. every .xml/.xsp parses
  4. a widget's declared sort matching what its source actually sorts by

Advisory checks — real findings, but the fix belongs in Weblate rather than in a
commit, so they are reported and never fail the build:

  5. .po: locale msgid differing from en_gb, and ids missing from a locale
  6. .po: Kodi markup tokens ([B], [CR], [COLOR]...) unbalanced between msgid/msgstr

Translations arrive from translate.osmc.tv and a commit that edits them by hand
is overwritten on the next sync, so failing a build on them would only train
people to ignore the check.

Deliberately NOT checked: "defined but never used". A structural parse cannot see
names reached through <param name="x">Name</param> element text or through quoted
expressions, and a from-scratch implementation reported 111 dead includes against
a true count of 14. It would be ignored within a week.

Usage:
    validate_skin.py [--warn-only] [repo_root]

Exit status is 1 when a check fails, unless --warn-only is given.
"""

import os
import re
import sys
import xml.etree.ElementTree as ET
from collections import defaultdict

# Generated at runtime by script.skinshortcuts; not in the tree.
SKIP_FILES = {os.path.join("xml", "script-skinshortcuts-includes.xml")}

DEFINITION_RE = re.compile(r"<(include|variable|expression)\s+name=\"([^\"]+)\"")
INCLUDE_TEXT_RE = re.compile(r"<include(?:\s+condition=\"[^\"]*\")?\s*>([^<$][^<]*)</include>")
INCLUDE_CONTENT_RE = re.compile(r"<include[^>]*\scontent=\"([^\"]+)\"")
VAR_RE = re.compile(r"\$VAR\[([^\],]+)")
EXP_RE = re.compile(r"\$EXP\[([^\]]+)")

WIDGET_RE = re.compile(r"<widget name=\"([^\"]+)\"(.*?)</widget>", re.S)
ITEM_RE = re.compile(r"<item name=\"([^\"]+)\"([^>]*)>(.*?)</item>", re.S)
PATH_RE = re.compile(r"<path>([^<]*)</path>")
SORTBY_RE = re.compile(r"<sortby>([^<]*)</sortby>")
SORTORDER_RE = re.compile(r"<sortorder>([^<]*)</sortorder>")
SEED_SORTBY_RE = re.compile(r"name=\"widgetSortBy\">([^<]*)<")
SEED_SORTORDER_RE = re.compile(r"name=\"widgetSortOrder\">([^<]*)<")
PLAYLIST_RE = re.compile(r"special://skin/(\S+\.xsp)$")

PO_CTXT_RE = re.compile(r'^msgctxt\s+"#(\d+)"', re.M)
MARKUP_RE = re.compile(r"\[/?(?:B|I|CR|UPPERCASE|LOWERCASE|CAPITALIZE|COLOR[^\]]*|LIGHT)\]")


def xml_files(root):
    """Every tracked .xml/.xsp under the repo, minus generated ones."""
    for base, dirs, names in os.walk(root):
        dirs[:] = [d for d in dirs if d != ".git"]
        for name in names:
            if not name.endswith((".xml", ".xsp")):
                continue
            path = os.path.join(base, name)
            if os.path.relpath(path, root) in SKIP_FILES:
                continue
            yield path


def check_parse(root):
    """5. Every XML file is well-formed."""
    problems = []
    for path in xml_files(root):
        try:
            ET.parse(path)
        except ET.ParseError as exc:
            problems.append("%s: %s" % (os.path.relpath(path, root), exc))
    return problems


def collect_names(root):
    """Return (definitions, duplicates, references) across the skin's XML."""
    definitions = set()
    duplicates = []
    references = defaultdict(list)  # name -> [(relpath, lineno)]

    for path in xml_files(root):
        rel = os.path.relpath(path, root)
        with open(path, encoding="utf-8") as handle:
            text = handle.read()

        seen_here = {}
        for lineno, line in enumerate(text.splitlines(), 1):
            for kind, name in DEFINITION_RE.findall(line):
                definitions.add(name)
                if name in seen_here:
                    duplicates.append((rel, name, seen_here[name], lineno))
                else:
                    seen_here[name] = lineno

            for pattern in (INCLUDE_TEXT_RE, INCLUDE_CONTENT_RE, VAR_RE, EXP_RE):
                for name in pattern.findall(line):
                    name = name.strip().lstrip("!")
                    # Names built at runtime from $PARAM/$VAR can't be resolved statically.
                    if not name or "$" in name:
                        continue
                    references[name].append((rel, lineno))

    return definitions, duplicates, references


def check_references(root):
    """1 + 2. Dangling references, and names defined twice in one file."""
    definitions, duplicates, references = collect_names(root)

    dangling = []
    for name in sorted(references):
        if name not in definitions:
            for rel, lineno in references[name]:
                dangling.append("%s:%d: references undefined name %r" % (rel, lineno, name))

    dupes = [
        "%s: %r defined at line %d and again at line %d (Kodi keeps the first, silently)"
        % (rel, name, first, second)
        for rel, name, first, second in duplicates
    ]
    return dangling, dupes


def playlist_order(root, path):
    """The <order> a bundled smart playlist sorts itself by, if it is one of ours."""
    match = PLAYLIST_RE.match(path.strip())
    if not match:
        return None
    full = os.path.join(root, *match.group(1).split("/"))
    if not os.path.exists(full):
        return None
    try:
        order = ET.parse(full).getroot().find("order")
    except ET.ParseError:
        return None
    if order is None or not order.text:
        return None
    return (order.text.strip(), order.get("direction") or "ascending")


def check_widget_sorts(root):
    """A widget's sort has to say the same thing everywhere it is written down.

    It is written down up to three times: the bundled playlist's own <order>, the
    widget definition the picker copies onto an item, and the menu seed. The add-on
    re-derives a widget's path, type and target on every build but never its sort,
    so nothing keeps the three in step. A disagreement is invisible from the skin --
    the widget still fills -- but the row sorts one way while the management dialog
    says another, and a seed that omits what its definition declares leaves the
    dialog blank for the seeded copy of a widget a picked copy would populate.
    """
    problems = []
    widgets_path = os.path.join(root, "shortcuts", "widgets.xml")
    if not os.path.exists(widgets_path):
        return problems

    with open(widgets_path, encoding="utf-8") as handle:
        text = handle.read()

    declared = {}
    for name, body in WIDGET_RE.findall(text):
        sortby = SORTBY_RE.search(body)
        sortorder = SORTORDER_RE.search(body)
        if bool(sortby) != bool(sortorder):
            problems.append("shortcuts/widgets.xml: %s declares a sort %s"
                            % (name, "field with no direction" if sortby
                               else "direction with no field"))
            continue
        declared[name] = (sortby.group(1), sortorder.group(1)) if sortby else None

        path = PATH_RE.search(body)
        own = playlist_order(root, path.group(1)) if path else None
        if own and declared[name] and declared[name] != own:
            problems.append(
                "shortcuts/widgets.xml: %s declares %s/%s but %s orders by %s/%s"
                % (name, declared[name][0], declared[name][1],
                   os.path.basename(path.group(1)), own[0], own[1]))

    menus_path = os.path.join(root, "shortcuts", "menus.xml")
    if not os.path.exists(menus_path):
        return problems
    with open(menus_path, encoding="utf-8") as handle:
        text = handle.read()

    for name, attrs, body in ITEM_RE.findall(text):
        widget = re.search(r'widget="([^"]+)"', attrs)
        if not widget or widget.group(1) not in declared:
            continue
        sortby = SEED_SORTBY_RE.search(body)
        sortorder = SEED_SORTORDER_RE.search(body)
        seeded = (sortby.group(1), sortorder.group(1)) if sortby and sortorder else None
        wanted = declared[widget.group(1)]
        if seeded != wanted:
            problems.append(
                "shortcuts/menus.xml: %s seeds %s but the %s definition declares %s"
                % (name,
                   "%s/%s" % seeded if seeded else "no sort",
                   widget.group(1),
                   "%s/%s" % wanted if wanted else "none"))
    return problems


def parse_po(path):
    """Return {id: (msgid, msgstr)} for the live (non-obsolete) entries."""
    entries = {}
    with open(path, encoding="utf-8") as handle:
        lines = handle.read().splitlines()

    current = None
    field = None
    buf = {"msgid": "", "msgstr": ""}
    for line in lines:
        if line.startswith("#~"):
            continue
        ctxt = PO_CTXT_RE.match(line)
        if ctxt:
            if current is not None:
                entries[current] = (buf["msgid"], buf["msgstr"])
            current = ctxt.group(1)
            buf = {"msgid": "", "msgstr": ""}
            field = None
        elif line.startswith("msgid "):
            field = "msgid"
            buf[field] += line[6:].strip().strip('"')
        elif line.startswith("msgstr "):
            field = "msgstr"
            buf[field] += line[7:].strip().strip('"')
        elif line.startswith('"') and field:
            buf[field] += line.strip().strip('"')
        elif not line.strip():
            field = None

    if current is not None:
        entries[current] = (buf["msgid"], buf["msgstr"])
    return entries


def check_translations(root):
    """3 + 4. Locale msgid drift, missing ids, and unbalanced Kodi markup."""
    lang_dir = os.path.join(root, "language")
    source = os.path.join(lang_dir, "resource.language.en_gb", "strings.po")
    if not os.path.isfile(source):
        return [], []

    en = parse_po(source)
    stale, markup = [], []

    for name in sorted(os.listdir(lang_dir)):
        if name == "resource.language.en_gb":
            continue
        path = os.path.join(lang_dir, name, "strings.po")
        if not os.path.isfile(path):
            continue

        locale = parse_po(path)
        rel = os.path.relpath(path, root)

        missing = sorted(set(en) - set(locale), key=int)
        if missing:
            stale.append("%s: %d id(s) missing from en_gb: %s"
                         % (rel, len(missing), ", ".join("#" + i for i in missing[:8])
                            + (", ..." if len(missing) > 8 else "")))

        for msgid_num, (msgid, msgstr) in sorted(locale.items(), key=lambda kv: int(kv[0])):
            if msgid_num not in en:
                continue
            if msgid != en[msgid_num][0]:
                # A stale source string with a live translation renders the OLD text.
                severity = "renders outdated text" if msgstr else "falls back to English"
                stale.append("%s: #%s msgid differs from en_gb (%s)" % (rel, msgid_num, severity))
            if msgstr and sorted(MARKUP_RE.findall(msgid)) != sorted(MARKUP_RE.findall(msgstr)):
                markup.append("%s: #%s Kodi markup tokens differ between msgid and msgstr"
                              % (rel, msgid_num))

    return stale, markup


def main(argv):
    warn_only = "--warn-only" in argv
    args = [a for a in argv[1:] if not a.startswith("-")]
    root = os.path.abspath(args[0]) if args else os.getcwd()

    dangling, dupes = check_references(root)
    blocking = [
        ("Malformed XML", check_parse(root)),
        ("References to names that are never defined", dangling),
        ("Names defined twice in one file", dupes),
        ("Widget sorts that disagree with their source", check_widget_sorts(root)),
    ]

    stale, markup = check_translations(root)
    advisory = [
        ("Translation source drift", stale),
        ("Kodi markup mismatch in translations", markup),
    ]

    def report(groups, label):
        total = 0
        for title, problems in groups:
            if not problems:
                print("ok    %s" % title)
                continue
            total += len(problems)
            print("%s  %s (%d)" % (label, title, len(problems)))
            for problem in problems:
                print("        %s" % problem)
        return total

    failed = report(blocking, "FAIL")
    print("")
    advisories = report(advisory, "note")

    print("")
    if advisories:
        print("%d translation advisory finding(s). These are fixed in Weblate, not in a"
              % advisories)
        print("commit -- a hand-edit here is overwritten on the next sync -- so they never")
        print("fail the build.")

    if not failed:
        print("No blocking problems.")
        return 0

    print("%d blocking problem(s) found." % failed)
    if warn_only:
        print("--warn-only given; not failing the build.")
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
