# DESIGN.md

The visual rules of skin.osmc, for anyone changing how it looks. Every value here is read from the
`PiersPort` branch; where this file and the XML disagree, the XML wins and this file is out of date.
The illustrated version, with rendered screens, is the *OSMC Skin Design Guide*.

Structural rules (coordinate families, numbering, the four aspect variants, translations) live in
`CLAUDE.md`. This file covers what things look like and why.

---

## 1. Principles

1. **Focus is scale, weight and opacity — not a fill.** A focused row grows, turns bold and goes to 100%
   white, with a fading underline. Unfocused is the same white at 50%. The accent colour appears only on
   selection markers and progress.
2. **Artwork leads, text gives way.** Narrower screens lose text width, never image size.
3. **One safe area, every ratio.** 120 px left and right, 100 px bottom, on all four canvases.
4. **Hint the non-obvious, nothing else.** Anything reachable but not visible gets a quiet arrow;
   anything visible gets none.
5. **One file, many states.** Textures are white shapes in alpha; colour, focus and dimming come from
   `colordiffuse`. No FO/NF pairs unless the shape changes (§14), no baked fades.
6. **No new sizes.** Seventeen font steps and one 66 px row height already exist. Take the nearest.

---

## 2. Colour

### Tokens (ARGB — alpha leads, the reverse of CSS)

| Variable | Value | Role |
| --- | --- | --- |
| `TextColorFO` | `FFFFFFFF` | Focused text |
| `TextColorNF` | `80FFFFFF` | Unfocused text (50%) |
| `OverlayColorFO` | `FFFFFFFF` | Focused icons, OSD buttons |
| `OverlayColorNF` | `55F1F1F1` | Unfocused icons, hints, dividers |
| `DarkenColor` | `60000000` | Darkening over artwork |
| `InvalidColor` | `60000000` | Edit control, invalid input |
| `OSDCacheColor` | `33FFFFFF` | Seek bar cache segment |
| `MaskingColor` | `FF000000` | Masking bars |
| `SolidBackgroundColor` | `FF000000` | Window clear |
| `SelectedColor` | per scheme | Accent: selection, progress |
| `BackgroundColor` | per scheme | Window overlay |
| `MenuOSDColor` | per scheme | Menu and OSD panels |
| `DisabledColor` | per scheme | Disabled text — grey, not dimmed white |

`colors/defaults.xml` holds the Lightblue values as a fallback; `xml/Variables_Colours.xml` is what
resolves at runtime. Every token can be overridden through `Skin.String(color.*)`; eleven pickers in
`SkinSettings.xml` all read the palette `extras/colors/colors.xml` (live data — do not trim it).

### The ten schemes

A scheme swaps accent, panel and disabled grey. Nothing else.

| Scheme | Selected | Background / MenuOSD | Disabled |
| --- | --- | --- | --- |
| **OSMC Lightblue** (default) | `FF00D7C7` | `FF009CC7` | `E65D5D5D` |
| OSMC Blue | `FF29B6EB` | `FF293FEB` | `808C8C8C` |
| OSMC Black | `FFC4A63A` | `FF404040` | `808C8C8C` |
| OSMC Rose Red | `FFF02D61` | `FFC41141` | `808C8C8C` |
| Sunset Yellow | `FFFFFC43` | `FFA6A41B` | `BF5D5D5D` |
| Lime Green | `FF72FF88` | `FF3FB551` | `E65D5D5D` |
| Dark Blue | `FF2E8CB0` | `FF15455C` | `808C8C8C` |
| Orange | `FFFF8536` | `FFC75C16` | `808C8C8C` |
| Red | `FFFF191E` | `FFA30003` | `808C8C8C` |
| Purple | `FFBF0360` | `FF850096` | `808C8C8C` |

A fresh install is Lightblue (set by `Includes.xml` when no scheme flag exists). Accent over panel must
stay legible in every scheme; Sunset Yellow and Lime Green are the tightest. Check new accent uses there.

### Overlay

Windows draw a two-shade overlay over background and fanart: `Background2*` (146 grey) on the content
side and `Background1*` (93 grey), both tinted `BackgroundColor`. The split follows the view: vertical at
698 (list, wall + info), 470 (home), horizontal at 824 (wide), 857 (wall), 912 (wide low). Opacity is
the *Background opacity* setting (Low · Medium · High · Highest). *Disable two-shaded overlay* uses one
shade throughout.

### Artwork

- **Background fanart** fills the screen with `aspectratio scale`: aspect kept, edges may crop.
- **Fanart and art inside a view box** use `keep`: whole image, original aspect, uncovered parts of the
  box stay transparent. No frame, no fill behind it.
- **Unfocused art** is dimmed by *Dim factor* (0–133%, default 100%) via `DiffusePosterNF` and friends.

---

## 3. Type

Source Sans Pro, in regular, bold, light and italic. **The name is a label, not a size** — read the `<size>`.

### Scale and line heights (px, at 1080p)

Line height = `round(1.257 × size) × linespacing` (font metrics: ascender 984, descender −273, gap 0).
`Font25` and all `-title` fonts use linespacing 1.3.

| Font | Size | Line | 2 lines | 3 lines | 4 lines | Scroll speed |
| --- | --- | --- | --- | --- | --- | --- |
| Font120 | 120 | 151 | 302 | 453 | 604 | 212 |
| Font72 | 68 | 85 | 170 | 255 | 340 | 120 |
| Font50 | 50 | 63 | 126 | 189 | 252 | 88 |
| Font48 | 46 | 58 | 116 | 174 | 232 | 81 |
| Font42 | 40 | 50 | 100 | 150 | 200 | 71 |
| Font36 | 34 | 43 | 86 | 129 | 172 | 60 |
| Font33 | 31 | 39 | 78 | 117 | 156 | 55 |
| Font30 | 28 | 35 | 70 | 105 | 140 | 49 |
| Font29 | 26 | 33 | 66 | 99 | 132 | 46 |
| Font27 | 25 | 31 | 62 | 93 | 124 | 44 |
| Font25 | 23 | 37.7 | 76 | 114 | 151 | 41 |

Wall-title fonts (on-artwork titles, one per strip height; the `-title` suffix stops a clash with
Kodi's own lower-case `font13`):

| Font | Size | Line | Arial size |
| --- | --- | --- | --- |
| Font13-title | 11 | 18.2 | 8 |
| Font16-title | 14 | 23.4 | 11 |
| Font18-title | 16 | 26 | 13 |
| Font20-title | 18 | 29.9 | 15 |
| Font23-title | 21 | 33.8 | 18 |
| Font26-title | 24 | 39 | 21 |

Scroll speed = `round(1.765 × size)`, so text moves at the same pace relative to its size.

### Rules

- **Textbox height = n × line, rounded up.** A textbox draws whole lines only; a box between two values
  shows the lower count and leaves the rest empty; a box shorter than one line shows nothing. Use the
  1-line value as the minimum height for labels, so descenders survive scrolling.
- **Plot boxes must hold at all four plot sizes.** View 511: S 189 (6 × 31), M 177 (5 × 35),
  L 161 (4 × 39), XL 172 (4 × 43). New plot boxes follow the same pattern — one height per size.
- **Never add a font size.** An eighteenth step must be declared in both fontsets and hold at four shapes.
- **The Arial fontset is not a swap.** Every size drops and `aspect 0.92` condenses it; text sized to
  fill a box in one set will not fill it in the other.
- Other faces: `SystemInfo` (Source Code Pro 24, only monospace), `International` (Arial 31, legacy).

---

## 4. Grid

| Ratio | Canvas | Content | Gutter | Bottom |
| --- | --- | --- | --- | --- |
| 16:9 | 1920 × 1080 | 1680 | 120 | 100 |
| 21:9 | 2560 × 1080 | 2320 | 120 | 100 |
| 21:9 masked | 2560 × 1440 | 2320 | 120 | 280 |
| 4:3 | 1440 × 1080 | 1200 | 120 | 100 |

- 21:9 keeps the left edge and moves right-hand content out; 4:3 narrows it.
- Masked draws on a 2560 × 1440 canvas with everything 180 px lower, between two 287 px bars that slide
  to the chosen ratio (2.40:1 default; 187 px on the canvas). Masking is gated off in `Expressions.xml`
  until its branch lands.
- **Exception:** the OSD bar is inset 150 px, not 120, so it floats over video.
- Every 16:9 widget box ends at x = 1800 (the safe edge).

---

## 5. Focus and states

| State | Treatment |
| --- | --- |
| Focused | `TextColorFO`, bold, larger (list 51: 72 → 144 px row, Font36-light → Font72-bold), underline, `FocusZoomAnimation` 90 → 100 |
| Unfocused | `TextColorNF` (50%), regular or light |
| Control group unfocused | Fades to 50% over 200 ms, cubic-out (`NonFocusWindowFadeAnimation`) |
| Disabled | `DisabledColor` — the one state outside the opacity system |

The two 50% fades stack to 25% on purpose. Unfocused text is therefore never the only carrier of meaning.

### The underline

- A **3 px image control**, top 8 px above the row's bottom (main menu: top 89 in 97; sub menu: 44 in 52).
  Never a row-tall texture with the line painted at its foot.
- `focusline.png` (20 × 3) for left-aligned text: opaque left, fades right.
  `focuslinecenter.png` for centred text: peaks centre, fades both ways. Centred uses give an explicit `top`.
- Tinted `TextColorFO`, stretched to the label width. The fade lives in the alpha.
- With *Disable underline text highlight* on, both variables resolve empty and `buttonfocus` becomes
  `00FFFFFF`; focus is then text alone.

---

## 6. Controls

`Defaults.xml` sets every control type once. A control that overrides a default should have a reason.

| Type | Size | Font | Notes |
| --- | --- | --- | --- |
| button | 400 × 66 | Font33 | No unfocused texture: an unfocused button is text alone |
| togglebutton | 400 × 66 | Font33 | Plus alt textures |
| radiobutton | 400 × 66 | Font33 | textwidth 362, radio 16 × 16 |
| spincontrolex | 400 × 66 | Font33 | textwidth 335, spin 43 × 60 |
| sliderex | 400 × 66 | Font33 | textwidth 120, slider 230 × 20 |
| slider | 360 × 20 | — | OSDSliderBack + nib, border 10,0,10,0 |
| colorbutton | 183 × 66 | Font33 | swatch 43 × 43 |
| edit | w × 66 | Font33 | invalidcolor `InvalidColor` |
| label | w × 36 | Font33 | aligny center, no scroll |
| fadelabel | w × 36 | Font33 | scroll, pauseatend 5000 |
| textbox | — | Font27 | autoscroll 8000 / 4000 / 12000 |
| progress | w × 44 | — | Stock textures cleared |
| fixedlist | — | — | preloaditems 2, scrolltime 240 sine-out |

- **66 is the row height.** Buttons, radios, spins, sliders, edits, colour buttons and settings dividers
  share it, so mixed columns align.
- Every default ends with `<include>WindowDepth</include>`; a new default without it sits at the wrong
  depth in 3D.

---

## 7. Views

Nineteen views; the id encodes the family.

| Family | Ids | Control |
| --- | --- | --- |
| List | 50, 51 (default), 511 (+ info) | fixedlist |
| Wide | 52, 521, 522, 523, 524 (low), 525 (low + info) | fixedlist |
| Wall | 53, 531–535, 536 (+ info), 537 (small), 538 (small + info), 539 (low) | panel |

Each view is a pair: `ViewtypeNN.xml` (controls) and `Coordinates_ViewtypeNN.xml` (four geometries).
Ten are offered as add-on defaults through `DefaultVideosView*`.

View 51 at 16:9: art at 120, 225, 405 × 600; list at 750, 1050 × 720. At 4:3 the list drops to 570 wide
and the art is unchanged.

Every view carries: window title and folder (top left), clock (top right), media flags (bottom left),
item count (bottom right), list indicators and scrollbar, and year · genre beside the title where there
is room.

---

## 8. Home

- Main menu: list 9000 at 120, 240, 300 × 679; rows 300 × 97, Font50-light → Font50-bold.
- Sub menu: list 9001, rows 410 × 52, Font33. Shows its own focus only while it holds focus; does not scroll.
- Logo 50 × 50 at 120, 105. RSS pinned to the bottom edge, full canvas width.
- Only the masked variant moves (180 px down); the other three bodies are identical.
- Without `script.skinshortcuts`, `xml/script-skinshortcuts-static.xml` supplies the default menu.

### Top-right corner

Clock by default; *Show date above system time* adds the date above in Font33 light. During playback the
now-playing title replaces the clock. A notification, the volume bar, an extended progress dialog or
caching hides the clock group (slides 120 px right, fades, 200 ms); a notification slides in 550 px from
the right in 200 ms on `MenuOSDColor`, with icon, Font27 heading and Font27 light message.

### Widgets

| Layout | Slot | Art, unfocused | Title strip | Box 16:9 (left, top · width) |
| --- | --- | --- | --- | --- |
| Poster (fallback) | 240 × 360 | 216 × 324 | 24 · Font23-title | 588, 340 · 1212 |
| Wide | 320 × 240 | 288 × 216 | 32 · Font30 | 520, 460 · 1280 |
| Square | 320 × 320 | 288 × 288 | 32 · Font30 | 520, 380 · 1280 |
| Square small | 240 × 240 | 216 × 216 | 24 · Font23-title | 588, 460 · 1212 |

- Unfocused art is 90% of its slot; focused fills it (the same 90 → 100 step as `FocusZoomAnimation`).
- A box holds whole slots only; a partial slot makes the row scroll a column early.
- *Show two widgets on screen* stacks two rows with smaller slots and title fonts
  (poster 173 × 222 slot, 133 × 200 → 148 × 222 art, Font16-title); every poster's bottom lands at y = 445.

---

## 9. Wayfinding

A remote has no cursor, so anything reachable but off screen is announced by an arrow at the nearest edge,
pointing the way to press.

| Hint | Texture | Size | Shown while |
| --- | --- | --- | --- |
| More list above / below | `up.png`, `down.png` | 30 × 16 | `Container.HasPrevious` / `HasNext` |
| Sub menu, off left | `sub-menu-left.png` | 30 × 30 | list and wall views |
| Sub menu, below | `sub-menu-down.png` | 30 × 30 | wide views |
| Dialog button row | `sub-menu-left/right.png` | 30 × 30 | `!ControlGroup(9001).HasFocus` |

- Always `OverlayColorNF` — quieter than anything focusable.
- Always conditional on *not* being there already.
- The arrow shows the **key press**, not the destination: the settings dialog reaches its button row with
  left/right, so the arrows sit at mid-height on both edges.
- Entry motion rehearses the press: edge hints slide in from their edge; list arrows travel 10 px the way
  they point.
- Kiosk mode suppresses sub-menu hints.

---

## 10. Icons and textures

| Tier | Authored size | Files |
| --- | --- | --- |
| List icon | 405 × 405 | `media/Default*.png` |
| OSD button | 60 × 60 | `media/osd/OSD*NF.png` |
| Hint arrow | 30 × 30 | `media/sub-menu-*.png` |
| List indicator | 30 × 16 | `media/up.png`, `down.png` |
| Status overlay | 30 × 30 | `media/views/Overlay*.png` |
| PVR flag | 30 × 30 | `media/pvr/*.png` |
| Media flag | 30 × 26 (20 px glyph, 3 px stroke) | `Video`, `Audio`, `Subtitles`, `Duration` |

- **White, shape in alpha.** Colour, focus and dimming come from `colordiffuse`. A half-transparent NF
  copy tinted `OverlayColorNF` renders at a ninth of full strength.
- **File size = the largest box that draws it**, exactly (follow `width`/`height`, `fallback` params, and
  `$VAR[mediaImages]` up to 405 × 600; `keep` on a square draws at `min(w, h)`). Smaller is also wrong:
  52 px in a 50 px box is a rescale every frame.
- **Rendered from vector originals** kept outside the repo. Re-render when a box changes.
- One stroke weight, one vocabulary (one folder, one note, one magnifier), no shadows, antialiasing intact,
  one merged shape, ink inset from the canvas edge.
- One file per icon. Severity (error/warning/info) is carried by copy, not icon colour.
- Retired art goes to `unused/`, outside `media/`, so it never ships in `Textures.xbt`.
- **`Textures.xbt` shadows `media/`.** A changed PNG shows nothing until the bundle is repacked; a new PNG
  shows at once.

---

## 11. Playback OSD

| Part | Control | Position | Size |
| --- | --- | --- | --- |
| Bar | group | 150, 945 | 1620 × 60 (2260 at 21:9, 1140 at 4:3) |
| Seek | button 100 | 430, 890 | 920 × 20 |
| Transport | grouplist 29 | left in bar | 418 × 60 |
| Options | grouplist 30 | right 0 | 720 × 60, align right |

- Every button is 60 px tall; the row shares one baseline. 7 px transparent spacers split transport into
  seek · channel/play · speed · record. Focus opens on control 5 (play/pause).
- Up to fifteen option buttons, each visible only when it applies; right alignment keeps them flush.
- One texture per button; focus is tint (`OverlayColorFO` vs `OverlayColorNF`). An active speed toggle
  keeps the focused tint. Record swaps files (`OSDRecordOffNF` / `OSDRecordOnNF`) because the shapes differ.
- Opens with a 90 → 100 back-out zoom; options fade in after 200 ms.
- Music visualisation info: art left, a Now column (artist, album, track · title, genre, format),
  playlist position and the same progress bar as video.

---

## 12. Settings UI

- Category list 9000 at 120, 228, rows 300 × 66; content from left 550. Each category owns a grouplist
  (100 General … 800), visible only while its category has focus.
- Row includes: `coords16` button/label 1250 × 66; `coords17` radio/divider 1250 × 66;
  `coords18` colour button 1205 × 66 (room for the swatch).
- **Hide settings that don't apply** rather than disabling them.
- Long categories group with a plain label row and `common/Divider.png` tinted `OverlayColorNF`.
- Help text is written about the skin, never to the reader (see `CLAUDE.md`, Translations).

### Settings that change the look

New work must hold under every value of: colour scheme and custom colours, background and menu/OSD
opacity, two-shaded overlay, background image/colour/fanart, underline highlight, dim factor, plot font
size (S–XL), titles on artwork, watched status, user rating, media flags mode, item count, scrolling
label, scrollbars, two widget rows, date above clock, masking ratio, kiosk mode.

---

## 12a. Dialogs

- **Full-screen** (yes/no, progress, select, keyboard, info, welcome): `DialogBackgroundImage`, heading in the
  window-title slot with the clock at right, `DialogButtons` centred at y 914 — 66 tall, Font36, auto width,
  30 px gap, `focus.png`. Opens with `DialogZoomAnimation`.
- **Panel and corner** (context menu, extended progress, notification): the window stays visible. Context menu
  is a 550 px `MenuOSDColor` panel sliding in 460 px from the left, rows 410 × 52; `SubMenuAnimation`
  shifts the list 26 px per row short of 20 so it stays centred. Corner dialogs stack via `CornerWindowLift*`.
- **Waiting**: blocking = `DimOverlay` + 200 px `busy-slow.gif`; with a percentage = progress dialog
  (760 × 20 bar at y 867); background work = corner dialog with 60 px `busy-slow-small.gif`, never blocking.

## 12b. Other windows and list states

- Reuse the library frame (title/folder top left, clock top right, count bottom right, art at 120, list at 782).
  Own layouts only where needed: TV guide (grid 120, 174, 1680 × 606; channel column 450; rows 69; ruler 54;
  54 five-minute blocks), weather (six 280 px day columns), file manager (two 800 px panes).
- `Startup.xml` only forwards; the screensaver is an add-on (the skin supplies `Font120` for Digital Clock).
- Every view handles four states: empty (frame and a 0 count, no message), loading (busy dialog), parent folder
  (`..`, no media flags, not counted) and long titles (cut when unfocused, scroll or cut when focused).
  Item descriptions hide on `!Integer.IsEqual(Container.NumItems,0)` / `!ListItem.IsParentFolder`.

## 12c. Legibility

Contrast over pure white fanart through the 146-grey overlay (worst case):

| Scheme | Low FO / NF | High FO / NF | Highest FO / NF |
| --- | --- | --- | --- |
| OSMC Lightblue | 4.8 / 2.4 | 6.2 / 2.8 | 6.9 / 3.0 |
| OSMC Blue | 7.2 / 3.1 | 9.9 / 3.7 | 11.3 / 4.0 |
| OSMC Black | 8.0 / 3.4 | 11.4 / 4.2 | 13.2 / 4.6 |
| OSMC Rose Red | 7.3 / 3.1 | 9.6 / 3.5 | 10.8 / 3.7 |
| Sunset Yellow | 4.2 / 2.2 | 5.4 / 2.6 | 6.0 / 2.8 |
| Lime Green | 4.3 / 2.3 | 5.4 / 2.6 | 6.1 / 2.8 |
| Dark Blue | 8.1 / 3.4 | 11.5 / 4.2 | 13.3 / 4.5 |
| Orange | 5.5 / 2.6 | 7.3 / 3.1 | 8.3 / 3.3 |
| Red | 8.7 / 3.4 | 11.6 / 3.9 | 12.9 / 4.1 |
| Purple | 8.6 / 3.4 | 11.6 / 4.0 | 13.0 / 4.2 |

- Focused text passes 4.5:1 everywhere at High and above; unfocused text never does — it must never be the only
  carrier of meaning.
- Reading text from Font33 (31 px). Font27/Font25 only for secondary lines in fixed places. `-title` fonts only on artwork strips.
- Focus keeps at least two of weight, opacity, size and underline; colour alone never counts.

## 12d. Translations

- Every visible word via `$LOCALIZE` or a string id (source: `language/resource.language.en_gb/strings.po`, 31000 range).
- Size for English + 35%, or scroll. Button rows are auto width: the row must fit 1680 px (1200 at 4:3) in the
  longest language.
- Settings label and `label2` share one 1250 px box: keep values short.
- RTL text renders right-to-left inside its box; layouts are not mirrored.
- Scripts Source Sans can't draw use the Arial fontset — layouts must hold in both.

---

## 13. Motion

| Animation | ms | Tween | Effect |
| --- | --- | --- | --- |
| FocusZoomAnimation | 300 | back / out | zoom 90 → 100 |
| VisibleHiddenFadeAnimation | 200 | linear | fade, 70 ms delay in |
| SidePanelSlideAnimation | 200 | linear | slide −200 → 0 |
| CornerWindowAnimation | 200 | linear | slide 550 → 0 |
| OSDOpenCloseAnimation | 200 | back / out | zoom 90 → 100 + fade |
| DialogZoomAnimation | 300 | back / inout | zoom 70 → 100 + fade |
| OptionsAnimation | 300 | back / inout | zoom 70 → 100, fade 150 delay 150 |
| NonFocusWindowFadeAnimation | 200 | cubic / out | fade 100 → 50 |
| fixedlist scrolltime | 240 | sine / out | list scrolling |

Reuse these includes. Nothing moves faster than 200 ms or slower than 300 ms outside list scrolling.

---

## 14. Looks wrong, isn't

- **FontNN names ≠ sizes.** Fifteen of the eighteen numbered fonts render smaller than their name
  (Font120 and Font50 match; Kodi's own `font13` is 21 px); in the Arial set, seventeen of eighteen. Kept to
  avoid touching every window file. Read the size.
- **Three FO/NF texture pairs.** `osd/OSDSliderNibNF`/`FO` (a square split by a 4 px gap that closes on
  focus), `common/ScrollbarGripNF`/`FO` and `common/ScrollbarGripHorizontalNF`/`FO` (a 3 px grip that
  doubles to 6 px on focus). Focus changes the shape, so tint alone can't carry it, as with record (§11).
- **Media flags a pixel apart.** All four share a 30 × 26 box, but `Video.png` sits at top 5
  (`MediaFlags_coords3`) where the others sit at 6, and `Audio.png` / `Subtitles.png` shift left 2 px
  (`MediaFlags_coords6`). Optical adjustments, identical at all four ratios. Deliberate for now.
- **Four disabled greys.** Each scheme tunes `DisabledColor` against its own panel. Deliberate.
- **Masking is gated.** `Masking` is `False` and `NonMaskedCoordinates` forced true, so every
  `_21:9_masked` body is maintained but unreachable until the masking branch lands.

---

## Checklist for a visual change

- [ ] Holds at 16:9, 21:9, 21:9 masked and 4:3 (all four leaves written)
- [ ] Inside the 120 / 120 / 100 safe area
- [ ] Uses existing font steps; textbox heights are whole lines at every plot size
- [ ] Colours via `$VAR[...]` tokens, checked in Sunset Yellow and Lime Green
- [ ] Focus by weight, opacity and the 3 px fading underline — no fills
- [ ] Off-screen targets hinted in `OverlayColorNF`; on-screen ones not
- [ ] Textures white-in-alpha, authored at the exact drawn size, bundle repacked
- [ ] Motion from the shared animation includes
- [ ] Survives every visual setting listed in §12
- [ ] Handles empty, loading, parent-folder and long-title states
- [ ] Fits in the longest translation; button rows inside the safe area
