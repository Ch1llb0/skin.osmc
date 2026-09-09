# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

This is **skin.osmc**, the default Kodi skin shipped with OSMC (Open Source Media Center). It is not a
traditional software project — there is no build step, package manager, or test suite. The repo is a Kodi
skin addon: XML layout files, XML "coordinate" files, translation files, and media assets that Kodi's skin
engine parses directly at runtime. Changes are validated by loading the skin in Kodi/OSMC, not by running
commands in this repo.

## Repository layout

- `addon.xml` — Kodi addon manifest (id `skin.osmc`, version, dependencies on `xbmc.gui` and the optional
  `script.skinshortcuts` addon). Bump the `version` attribute and add a `<news>` entry here for releases.
- `Changelog.md` — human-readable changelog, grouped by version under `_New_` / `_Improved_` / `_Fixed_`
  headings. Update alongside `addon.xml` version bumps.
- `xml/` — all skin windows, dialogs, includes and variables (see architecture below).
- `colors/defaults.xml` — base color theme values referenced by `Variables_Colours.xml`.
- `language/resource.language.<locale>/` — per-locale translation strings, one folder per language.
- `media/` — icons/images referenced by skin XML via `<texture>`/`<icon>` (mostly `Default*.png`), plus
  `media/Textures.xbt`, the TexturePacker bundle of that same folder. `addon.xml` declares the bundle as
  `defaultthemename`, and Kodi checks bundles *before* the filesystem, so the loose files are shadowed at
  runtime: editing a PNG and reloading shows no change until the bundle is rebuilt, while *adding* one works.
- `fonts/` — TTF files declared in `xml/Font.xml`.
- `shortcuts/` — config for the `script.skinshortcuts` addon: `menus.xml` (menu and submenu structure),
  `widgets.xml`, `backgrounds.xml`, `properties.xml` (widget property pickers) and `templates.xml`.
- `extras/` — bundled smart playlists (`extras/playlists/*.xsp`), background images, debug grid overlays,
  and `extras/colors/colors.xml`.
- `resources/` — addon icon/fanart shown in the Kodi addon browser.

## Branch model (important — read before editing coordinates)

`PiersPort` is the development branch, developed at 1920x1080 16:9; `piers` and `omega` are the release
lines. There are **sibling branches for other aspect ratios/variants**: `omega-scope`, `omega-21to9`,
`omega-4to3`. Each sibling publishes under its own addon id — `skin.osmc.scope`, `skin.osmc.21to9`,
`skin.osmc.4to3` — so they are four separately installed Kodi addons, not one addon with four layouts.

**The siblings do not carry their own layout XML.** `git rev-parse origin/<branch>:xml` returns the same
tree hash for `omega`, `omega-21to9`, `omega-4to3` and `piers`; `omega-scope` differs by three lines of
`xml/Variables.xml`. Every branch already contains all four aspect variants of every coordinate include,
and which one applies is decided at load time by `Skin.AspectRatio`, which comes from the single uncommented
`<res>` in that branch's `addon.xml`. Note that `omega-scope` declares 2560x1440 `aspect="16:9"`, so it
selects the `_21:9_masked` leaves through `$EXP[MaskedCoordinates]` rather than the 21:9 ones.

So a coordinate change is made **once**, on the development branch, including all four aspect variants — do
not hand-edit `xml/` on a sibling, as it is propagated wholesale and an edit there is overwritten. The four
genuinely per-branch files are `addon.xml`, `README.md`, `CLAUDE.md` and `.github/`.

`.github/sync.yml` + `.github/workflows/sync-translations.yml` sync the `language/` folder out to the
siblings, so translation changes only need to be made once.

## Skin XML architecture

Kodi skin XML separates *layout logic* from *positioning*, and this skin leans on that split heavily:

- **Window/dialog files** (e.g. `xml/Home.xml`, `xml/MyVideoNav.xml`, `xml/DialogVideoInfo.xml`) define
  controls, visibility conditions, animations, and behavior, but reference positions indirectly via
  `<include>SomeName_coords</include>` rather than hardcoding `<left>`/`<top>`/`<width>`/`<height>`.
- **`xml/Coordinates_*.xml` files** (one per corresponding window/include file, e.g.
  `Coordinates_Home.xml`, `Coordinates_Includes_Widgets.xml`) define the actual `_coords` includes. Most
  coordinate includes branch on aspect ratio / masking state, e.g.:
  ```xml
  <include name="HomeLogo_coords">
      <include condition="$EXP[NonMaskedCoordinates]">HomeLogo_coords_16:9</include>
      <include condition="String.IsEqual(Skin.AspectRatio,21:9)">HomeLogo_coords_21:9</include>
      <include condition="$EXP[MaskedCoordinates]">HomeLogo_coords_21:9_masked</include>
      <include condition="String.IsEqual(Skin.AspectRatio,4:3)">HomeLogo_coords_4:3</include>
  </include>
  ```
  All `Coordinates_*.xml` files are pulled in via `xml/Includes.xml`.
- **`xml/Includes*.xml`** (no `Coordinates_` prefix, e.g. `Includes.xml`, `Includes_Widgets.xml`,
  `Includes_MediaFlags.xml`, `Includes_SubMenu.xml`) hold reusable, non-positional includes: animations,
  common control groups, widget templates, media flag rendering, etc.
- **`xml/Variables*.xml`** define `$VAR[...]` skin variables:
  - `Variables.xml` — general-purpose variables.
  - `Variables_Colours.xml` — resolves the active color scheme (theme color sets like
    `DefaultColorSetOSMCBlue`, or user-picked custom colors from `Skin.String(color.*)`) into concrete ARGB
    hex values used throughout the skin.
  - `Variables_Settings.xml` — variables derived from skin settings.
  - `Variables_Skinshortcuts.xml` — variables feeding the `script.skinshortcuts` main menu integration.
- **`xml/Viewtype5*.xml`** — the numbered library view layouts (list/wall/poster/fanart wall variants)
  selectable per media section.
- **`xml/Font.xml`** — the font set definitions (`FontNN`, plus `-bold`/`-light`/`-italic` variants) used
  everywhere else via `<font>FontNN</font>`.
- **`xml/script-skinshortcuts*.xml` / `xml/script-upnext-*.xml`** — integration layouts for the
  `script.skinshortcuts` and `script.upnext` addons.

When adding a new positioned element: add the control to the relevant window/include file referencing a new
`_coords` include name, then define that include (with aspect-ratio/masking branches as needed) in the
matching `Coordinates_*.xml` file, then ensure that file is pulled in via `xml/Includes.xml` if it isn't
already.

## Colors

Two layers control color:
1. `colors/defaults.xml` defines the base named colors (`TextColorFO`, `BackgroundColor`, etc.).
2. `xml/Variables_Colours.xml` resolves those into `$VAR[...]` variables used across the skin, taking into
   account the user's selected color scheme (`Skin.HasSetting(DefaultColorSetOSMCBlue)` etc.) or custom
   per-element overrides stored as `Skin.String(color.*)`.

`extras/colors/colors.xml` is **not** a sample scheme — it is the live palette the colour pickers read. It
holds 513 named colour values and is passed as the palette argument to all 11 `Skin.Setcolor` calls in
`xml/SkinSettings.xml`. It contains no skin-role names (`TextColorFO` and the like), so it cannot serve as an
override scheme; trimming or regenerating it empties every colour picker in the skin settings.

## Translations

Each `language/resource.language.<locale>/strings.po` supplies localized strings referenced in skin XML as
`$LOCALIZE[<id>]`. Only edit them on the development branch — they are synced outward to the sibling
branches by CI (see Branch model above), so edits made directly on a sibling will be overwritten.

**Translated content comes from Weblate**, at the project named in every `.po` header
(`X-Generator: Weblate`, and a `Language-Team` URL). Over a hundred commits in this repo are Weblate's, so a
commit that hand-edits a `msgstr` is overwritten on the next sync. The split to respect:

- **New source strings** go in `language/resource.language.en_gb/strings.po` in the normal commit, alongside
  the XML that uses them. String ids are **append-only**: take `max(id) + 1`, and never reassign a retired id,
  because Kodi keys on `msgctxt` alone and reusing an id silently repoints every locale's translation.
  Skin ids are confined to 31000-31999.
- **Translations** of those strings come back through Weblate. Do not PR them.

Changing an existing `msgid` invalidates every translation of it, so avoid cosmetic rewording — a hyphen
costs 26 retranslations.

## Verifying changes

There is no build step and no test suite. To verify a change, install the skin into a Kodi/OSMC instance (or
Kodi on desktop) pointed at this repo's directory and reload the skin, or package it as a zip and install via
Kodi's "install from zip file". Remember that `media/Textures.xbt` shadows the loose images, so a change to an
existing PNG needs the bundle rebuilt before it is visible.

What *is* automated is `.github/workflows/validate.yml`, which runs `.github/scripts/validate_skin.py` on
every pull request. It catches four things that fail silently:

- an `<include>` or `$VAR[]` name that is referenced but never defined — Kodi logs a warning at most for the
  first and nothing at all for the second
- a name defined twice in one file — Kodi keeps the first definition and discards the second in silence
- a file that does not parse — malformed XML silently fails to load the affected window
- a widget whose declared sort disagrees with its source — the widget still fills, so nothing looks wrong,
  but the row sorts one way while the management dialog says another

It also reports each locale's `msgid` against `en_gb` and the Kodi markup tokens (`[B]`, `[CR]`, `[COLOR]`)
between `msgid` and `msgstr`, but never fails on those, since they are Weblate's to fix.

The structural checks fail the build. The translation reports stay advisory either way, as a hand-edit
here is overwritten on the next Weblate sync.

Run it locally before committing — standard library only, no arguments beyond the repo root:

```sh
python3 .github/scripts/validate_skin.py .
```

It deliberately does **not** report definitions that are never used: names reached through
`<param name="x">Name</param>` element text or through a quoted expression are invisible to a structural
parse, and that check reports false positives by the hundred.

## The no-addon fallback (`xml/script-skinshortcuts-static.xml`)

`script.skinshortcuts` is an optional dependency. When it is installed **and enabled** it generates
`xml/script-skinshortcuts-includes.xml` into the skin folder (gitignored). When it is not,
`xml/script-skinshortcuts-static.xml` stands in. `xml/Includes.xml` picks between the two.

The static file holds **one default home menu layout, usable without the addon**. It is generated output
that happens to be committed — never hand-edit it, and never regenerate it from a Kodi whose menu has been
customised, or that customisation becomes everyone's default.

### Regenerating it

1. Start from a **clean profile**. This is the load-bearing step.
2. Install this skin and `script.skinshortcuts` v3, then let the addon build — `Home.xml` fires
   `RunScript(script.skinshortcuts,type=buildxml)` on load.
3. The addon writes `xml/script-skinshortcuts-includes.xml`. Copy it over
   `xml/script-skinshortcuts-static.xml` **verbatim**.
4. Note in the commit message which addon version it was built against. The committed file is a 3.0.3
   build; `addon.xml` pins 3.0.3. The floor is not cosmetic: `shortcuts/properties.xml` uses an
   `<overrides>` block to rename `widgetSortDirection`, and property overrides did not exist before 3.0.2,
   so on an older addon that rename is silently skipped.
5. Re-check the interface below still lines up, and run `xmllint --noout` on the result.

### When a rebuild is needed

The bar is that the fallback stays a *valid* default menu, not that it matches the current templates. So:

- **Must rebuild** — the change alters one of the 16 names the file defines (below), or removes/renames one
  of the 14 includes it calls into. Otherwise the no-addon path breaks or double-defines.
- **Should rebuild** — the change fixes a seeded *menu item* (an icon, a widget seed). Nothing breaks, but
  the fix never reaches the users this file exists for.
- **No rebuild** — everything else. Template refactors that keep the emitted names, changes to
  `Includes_Widgets.xml` (the fallback calls those includes by name, so fixes propagate for free),
  `<groupings>` and `widgets.xml` edits (picker-only), and all management-dialog work.

### The interface it sits in

It **defines**, for the skin to consume: includes `skinshortcuts-mainmenu`, `-mainmenu-submenu`,
`-template-vertical`, `-template-reloading`, `-template-widgetControl`, and one per menu (`-movies`,
`-tvshows`, `-music`, `-videos`, `-pictures`, `-tv`, `-radio`, `-disc`, `-settings`); plus the variables
`widgetDetails` and `widgetWeatherBackground`. It does **not** define `widgetBackground` — that name is
the skin's own, in `Variables_Skinshortcuts.xml`.

It **calls into**, and these must exist in `xml/Includes_Widgets.xml`: `weather-widget`, `widget-image`,
`widgetAnimation`, `widgetHeading`, `widgetOnControl`, `widgetOverlayBar`, the four `widgetLayout-*`
(`-tall`, `-square`, `-square-small`, `-weather`) and the four `widgetLayoutSlide-*` (same four suffixes).

To re-derive both lists from a build rather than trusting this one:

```sh
grep -o '<include name="[^"]*"' xml/script-skinshortcuts-static.xml | cut -d'"' -f2 | sort -u
{ grep -o '<include content="[^"$]*"' xml/script-skinshortcuts-static.xml | cut -d'"' -f2
  grep -o '<include>[a-zA-Z-]*</include>' xml/script-skinshortcuts-static.xml | sed 's/<[^>]*>//g'
} | sort -u
```
