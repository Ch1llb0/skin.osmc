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
- `media/` — icons/images referenced by skin XML via `<texture>`/`<icon>` (mostly `Default*.png`).
- `fonts/` — TTF files declared in `xml/Font.xml`.
- `shortcuts/` — config for the `script.skinshortcuts` addon (main menu / submenu structure, e.g.
  `mainmenu.DATA.xml`, `overrides.xml`, `template.xml`).
- `extras/` — bundled smart playlists (`extras/playlists/*.xsp`), background images, debug grid overlays,
  and an example custom color scheme (`extras/colors/colors.xml`).
- `resources/` — addon icon/fanart shown in the Kodi addon browser.

## Branch model (important — read before editing coordinates)

`omega` is the default/main branch for this repo, developed at 1920x1080 16:9. There are **sibling branches
for other aspect ratios/variants**: `omega-scope`, `omega-21to9`, `omega-4to3`. `.github/sync.yml` +
`.github/workflows/sync-translations.yml` automatically sync the `language/` folder from `omega` to those
branches on every push — so translation changes only need to be made once, on `omega`.

Everything else (layout/coordinate XML) is maintained independently per branch. When a change affects
positions or sizing, check whether it needs a parallel change on the other aspect-ratio branches — this repo
does not do that for you automatically.

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

`extras/colors/colors.xml` is a sample custom scheme demonstrating the override format end users can install.

## Translations

Each `language/resource.language.<locale>/strings.po` supplies localized strings referenced in skin XML as
`$LOCALIZE[<id>]`. Only edit translation content on the `omega` branch — it is synced outward to the other
aspect-ratio branches by CI (see Branch model above), so edits made directly on a sibling branch will be
overwritten.

## Verifying changes

There is no automated test/build/lint pipeline in this repo. To verify a change, install the skin into a
Kodi/OSMC instance (or Kodi on desktop) pointed at this repo's directory and reload the skin, or package it
as a zip and install via Kodi's "install from zip file". Check XML well-formedness before committing —
malformed XML will silently fail to load the affected window in Kodi without a clear error in this repo.

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
