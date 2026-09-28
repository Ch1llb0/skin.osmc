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
3. **One safe area, every ratio.** 120 px left and right, 100 px bottom, on all four canvases. Scrollbars
   are the one thing that may sit in the side gutter (§4).
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

**The split is rounded where the shades meet**: the bright part's two inner corners, at the screen edge, at
8 px (a vertical split's top-right and bottom-right, a bottom band's top-left and top-right, a band between
two dark parts all four); outer screen edges stay square. The bright part is drawn 9-slice from
`Background2*Right`, `*Top` or `*Round`, and under each rounded corner an 8 × 8 `Background1*Fill`
(flipped with `flipx`/`flipy` for the other corners) puts the dark shade where the rounding cuts the bright
one away. The fill's alpha is a(1−c)/(1−a·c), c being the bright tile's coverage, so the two composite to
exactly the mix of the shades at every pixel of the arc and nothing behind shows through; both shades keep
their old values everywhere else. Windows pass the geometry to `WindowBackgroundImage`; the dialogs share
`DialogBackgroundOverlay`. Masked 21:9 rounds a vertical split on the masked frame (y 180 and 1260), with
dark bands above and below it. With one shade there is no split, and the bright part is drawn plain.

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
- **Exception:** a scrollbar may sit in the left gutter, beside the content it scrolls rather than
  inside it: x 100 in the text viewer, x 90 in the file manager and the PVR guide, providers, search and
  timers windows. It is 20 px wide and carries no text, so nothing readable leaves the safe area.
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
- `focusline.png` (40 × 3) for left-aligned text: round, opaque left end, fades right; drawn with
  `border="2,0,0,0"` so the cap never stretches. `focuslinec.png` (`$VAR[focuslinecenter]`) for centred
  text: peaks centre and fades both ways to nothing, drawn with **no border**, so the whole fade stretches.
  A `2,0,2,0` border would freeze the two outer texels and stretch the 12.5 % one next to them across the
  last tenth of the line, which then stops short instead of fading out. Centred uses give an explicit `top`.
- **Button focus** textures (`common/focus`, `focus52`, `focusright`, `focus27c`, `focus52c`, `focus66c`) draw
  the same 3 px line at the foot of the button: 40 px wide, the same fades; `border="2,0,0,0"` (left) or
  `0,0,2,0` (right) so the round cap never stretches, and no border on the centred ones (`*c`), which
  have no cap to keep.
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
| spincontrolex | 400 × 66 | Font33 | textwidth 335, spin 35 × 66 (the arrows' own size) |
| spincontrol | 66 × 66 | Font33 | spin 35 × 66 (unused; draws each arrow at the control's own size) |
| sliderex | 400 × 66 | Font33 | textwidth 120, slider 230 × 20 |
| slider | 360 × 20 | — | OSDSliderBack + nib, border 10,0,10,0 |
| colorbutton | 183 × 66 | Font33 | swatch 43 × 43 |
| edit | w × 66 | Font33 | invalidcolor `InvalidColor` |
| label | w × 36 | Font33 | aligny center, no scroll |
| fadelabel | w × 36 | Font33 | scroll, pauseatend 5000 |
| textbox | — | Font27 | autoscroll 8000 / 4000 / 12000 |
| progress | w × 44 | — | Stock textures cleared |
| fixedlist | — | — | preloaditems 2, scrolltime 240 sine-out |

- **66 is the row height.** Buttons, radios, spins (the square spincontrol too), sliders, edits, colour
  buttons and settings dividers share it, so mixed columns align.
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
- Sub menu: list 9001, rows 390 × 52, Font33. Shows its own focus only while it holds focus; does not scroll.
- Logo 50 × 50 at 120, 105. RSS a rounded 48 px panel 20 px clear of the bottom, left and right edges; its
  36 px text line sits 6 px from the panel's top and bottom and 24 px in from each end
  (`HomeRSS_coords2`), so the scrolling text never runs into the edges or the corners. It is drawn before
  the rest of Home, so the side menu and its dim overlay lie over it, as every dialog does.
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
| More list above / below | `up.png`, `down.png` | 30 × 20 | `Container.HasPrevious` / `HasNext` |
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

### Grids

| Tier | Canvas | Live area | Stroke | Corner radius | Files |
| --- | --- | --- | --- | --- | --- |
| List icon | 405 × 405 | 300 (52.5 margin) | 15 | 16 | `media/Default*.png` |
| OSD button | 60 × 60 | 36 (12 margin), baseline 48 | 4 | 4 | `media/osd/OSD*.png` |
| Hint | 30 × 30 | 26 (2 px clear) | 3 | 2 | `sub-menu-*` |
| Status overlay | 32 × 32 | 26 of 30, scaled | 3 | 2 | `views/Overlay*`, `pvr/<size>/*` |
| Toast icon | 60 × 60 | 48 | 3 | — | `DefaultIconError`, `DefaultIconInfo`, `DefaultIconWarning` |
| List indicator | 30 × 20 | 26 × 15, 2 px clear | solid, 2 px round corners | — | `up.png`, `down.png` |
| Move buttons | 35 × 66 | 31 × 18, centred | solid, 2 px round corners | — | `common/ArrowUp`, `ArrowDown` |
| Media flag | 30 × 26 | 20 px ink box | 3 | 2.5 | `Video`, `Audio`, `Subtitles`, `Duration` |
| Rating strip | 238 × 36 | five 47.6 px cells | 3 | — | `rating0`–`rating5` |

`OverlaySpoiler.png` is not an overlay. No skin XML names it: Kodi itself returns it as `ListItem.Thumb` and
`ListItem.Icon` of an unwatched episode when the unwatched-episode thumbs are hidden and the show has no fanart
(`CFileItem::GetThumbHideIfUnwatched`). The views (`$VAR[mediaImages]`) and the video info dialog
(`$VAR[VideoInfoImage]`) catch that case themselves and show the show's fanart or `DefaultTVShows.png`, so it is
drawn only where a box reads `ListItem.Icon` directly: the Home widgets' no-poster fallback, square with `keep`
at 288, 216 (216 × 324 and 216 × 216), 177, 162 (162 × 197) and 133 (133 × 200 and 133 × 133), and the select
dialog's image at 405 (405 × 600) and 96 if it ever lists episodes. It is drawn on the list-icon grid at
405 × 405, to cover the select dialog, and scales down everywhere else.

Some files are sized by where they are drawn rather than by their tier, each at its largest box: the toast icons
at 60 (Kodi shows them only in the notification's 60 × 60 icon box), `DefaultMovie` at 400 (the 400 × 400 view
boxes), the rating strips at 238 × 36 (the info dialogs' 36 px rows), and `pvr/encrypted` at 405, since it
stands in for a channel's icon up to the PVR info dialog's 405 × 600. Their strokes are set so they land on the
tier's weight at that size (3 px at 60, 15 px at 400). `DefaultVideoExtras` (405) is the Extras entry Kodi adds
beside Versions when a movie's assets are listed: the Versions screen with a "more" badge.

Keylines on the 405 grid: circle 300, square 266, portrait 234 × 300, landscape 300 × 234.

OSD option glyphs are 3 px outlines in the 36 px live area of a 60 px button (x 12–48). Transport glyphs are
solid and flush in 36 × 60 boxes (see §11); the gaps come from the row, not the canvas. The Play and Pause
status images draw them at 36 × 60, placed so the glyph keeps its centre. The buttons themselves keep one size
and top.

Status overlays come in six tiers, each drawn at its own size (see Watched-status overlays and pointer).

### Drawing rules

- **Outline style.** One stroke weight per tier, round caps and joins, outlines only. Fills are for small
  details (dots, the play triangle, lamp, badge glyphs) and for direction-only arrows.
- **Lines never overshoot.** A line that meets a frame ends flat inside it.
- **Overlaps cut a gap.** Where one shape passes in front of another, the one behind is cut back so a clear
  gap remains: at least 7.5 px between strokes, 15 px around a badge ring. No touching strokes.
- **Arrows.** Direction-only hints (up, down, sub-menu, play, trick) are solid triangles with 2 px round
  corners: each is inset 2 px and drawn with a 4 px round-join stroke, so its outer size stays the sharp
  triangle's. Double trick triangles keep a hairline gap between the tips. Any arrow with a shaft gets an
  open head of two lines at 42°, pointing along the shaft or arc.
- **Badges.** Bottom right on the 405 grid: a 128 px ring centred at 300, 300, with a 15 px gap cut from the
  glyph behind. A badge exists only to tell two icons apart or to add context the glyph can't carry.
  Add-on types use the plain glyph; the add-on badge (puzzle) appears only where the glyph matches a library
  icon (AddonMusic, AddonPicture, AddonProgram, AddonVideo, AddonWeather, AddonPVRClient, AddonInfoProvider,
  GameAddons) or where the glyph alone doesn’t say it’s about add-ons (AddonsUpdates). Context badges: info, export, code, loop. Variants of one subject are one base glyph plus a badge (plus, clock, star,
  sort, stack, check, play, note, record, cross, 3/8 progress). Exception: AddonInfoLibrary's badge sits 10 px
  right.
- **The folder means a folder.** Only Folder and AddonsZip use it; add-on types never.
- **No text in icons.** Words and numbers become a glyph or a badge.
- **One glyph per subject.** Camera = movie library; horizontal screen with play = a video; stacked screen
  with play = TV shows; note = music; grooved record = albums; plain disc + play = video discs;
  tower = PVR sources; stopwatch = timers; speech bubble = lyrics, subtitles, language.
- **Colour** is never baked in — white shape in alpha, tinted by `colordiffuse`. Two exceptions: the red
  record lamp (OSDRecordOn/Off, pvr/Recording) and the dark keyline round the mouse pointer (`mouse`,
  `MouseClick`, `MouseDrag`), which keeps it visible over white.

### Files

- **White, shape in alpha.** Colour, focus and dimming come from `colordiffuse`. A half-transparent NF
  copy tinted `OverlayColorNF` renders at a ninth of full strength.
- **Export rules:** 100 % opacity, transparent pixels filled white (no dark fringe when Kodi scales), at
  least 2 px clear at the canvas edge, strokes on whole pixels.
- **NF suffix only where an FO file exists.** Single-version files carry no suffix.
- **File size = the largest box that draws it**, exactly (follow `width`/`height`, `fallback` params, and
  `$VAR[mediaImages]` up to 405 × 600; `keep` on a square draws at `min(w, h)`). Smaller is also wrong:
  52 px in a 50 px box is a rescale every frame.
- **Vector originals** are the SVGs in `osmc-icons-svg` (kept outside the repo): `icons-svg/` for icons,
  `textures-svg/` for the scrollbar, slider and progress textures, `busy-spinner/` for the spinner.
  `index.csv` maps each to its PNG and size; check every SVG's canvas against it before rendering.
  Re-render when a box changes. `logo.png` is the one exception: the 405 logo redrawn at 50 px with a 2 px
  stroke on whole pixels and the ring filling the box.

### Scrollbars, sliders and progress bars

- **Scrollbar**, 20 px control, centred on x 11 (y 9 horizontal): a 2 px track (x 10–12); the unfocused
  nib is the focused nib's shape (6 px, x 8–14, round ends) with the track's two columns cut out, a
  2 px half each side, so it reads as the same nib, only dim, while the translucent nib never lies over
  the track and the track never shows through; the focused nib is 6 px
  (x 8–14), opaque in `OverlayColorFO`, over both. The track and the unfocused nib take the control's
  `OverlayColorNF`; a texture with its own `colordiffuse` replaces the control's rather than multiplying it.
- **A scrollbar on the overlay split is centred on it:** the texture's centre line (x 11, y 9) is the split.
  The list views place the control at x 687 for the split at 698, wide at y 815 for 824, wide low at y 903 for
  912 (180 px lower when masked). The position is the same in both overlay styles: two-shade draws no track and
  the nib runs down the split; *Disable two-shaded overlay* draws the track where the split would be, with the
  nib centred on it. A scrollbar away from a split (settings profile, dialogs) keeps its own place.
- **Rounding keeps the old dimensions.** Progress and cache fill the full 20 px of their control and its
  whole length; the track (`OSDProgressBack`, 30 %) is round at both ends, the fill (`OSDProgressBar`) at its
  left end only (`border="10,0,0,0"`), so its moving end is straight and meets chapter markers square. The
  track is drawn once, as its own image, then the cache fill, then the play fill; neither bar draws a track of its
  own, or the later one's would cover the earlier fill (the cache's 30 % over the play fill read as 51 %). The
  slider track is 4 px and full length; slider nibs are 16 × 16 at 4 px radius, solid, the unfocused one
  with the track's four rows (y 8–12) cut out so the track never shows through it, the focused one opaque
  over the track; the big nib 6 × 30.
- **A bar at the foot of a panel follows the panel's corners.** The corner dialogs (extended progress,
  cache, Up Next) draw a 12 px bar inside the panel: 10 px below the last line of text or buttons, 12 px
  clear of the panel's left and right edges and its bottom, so 526 wide in the 550 px panel.
  Track `common/PanelProgressBack` (30 %, round at both ends, `border="6,0,6,0"`), fill
  `common/PanelProgressBar` (round left end, square right end, `border="6,0,0,0"`), so the fill's moving end
  is a straight cut. The panels grow to hold it (extended progress 94, cache 64, Up Next 131, simple 101), and
  `CornerWindowLift*` steps by a panel's height plus the 10 px gap (cache 74, progress 104). The progress
  dialog keeps its 760 × 20 bar at y 867, inside the safe area.
- **Settings separators** (`common/Divider.png`): the 3 px line at 50 % with round ends inside the 2 px
  border columns.
- One file per icon. Severity (error/warning/info) is carried by copy, not icon colour.
- Retired art goes to `unused/`, outside `media/`, so it never ships in `Textures.xbt`.
- **`Textures.xbt` shadows `media/`.** A changed PNG shows nothing until the bundle is repacked; a new PNG
  shows at once.

### Corner radius (on screen, 1920 × 1080)

| Element | Radius |
| --- | --- |
| Panels and dialog backgrounds with visible corners (OSD bar, notifications, corner dialogs, side menus, context menu, sub-menus, the select dialog's bottom panel, the scrolling index; busy/progress panels; full-screen dialogs while they zoom) | 8 px |
| Art 100 px or larger (covers, posters, thumbs, logos, widgets, OSD and notification thumbnails) | 8 px |
| Art under 100 px, colour swatches and small solid elements up to 36 px (list-row icons, nibs, focus boxes) | 4 px |
| Thin bars up to 20 px tall (progress, seek, cache, slider tracks, scrollbars) | fully round (half the height) |
| Full-screen overlays | none at the screen edge; 8 px where the bright shade meets the dark one |

- Kodi has no corner radius on an image control, so a rounded surface is a rounded texture drawn 9-slice.
  Floating MenuOSD panels draw `$VAR[MenuOSDPanel]` (`common/Panel{Low,Medium,High,Highest}.png`: the
  `Background2*` grey and alpha with 8 px corners) with `border="8"`. `Background1/2*` stay plain (24 px, so a
  9-slice border on them stays inside the texture) and draw the overlays' dark parts and one-shade mode.
- **A panel that slides in from an edge floats 20 px clear of every edge it touches**, rounded on all four
  corners, and slides just far enough to start off screen. **Its content moves in with it**, keeping the
  distance it had from the panel's edges. Side menus, the context menu and sub-menus sit at 20, 20,
  430 × 1040 (masked top 200): their right edge is 20 px short of the 470 split of the home and settings
  overlay, mirroring the 20 px to the screen edge, and the 460 px slide hides them. The rows are 390 wide
  at x 40, 20 px clear of each side as the panel is of the screen edge; sub-menu buttons and radio buttons
  take that width from `SubMenu_coords5`/`6` rather than the 400 px button default. The list area is 988 tall, 19 whole rows of 52, so no row is
  ever cut, 26 px inside the panel at the top and bottom (46; 36 where two spacers lead); the
  `SubMenuAnimation` shift is 26 px per row short of 19. Corner dialogs are 550 wide with their right edge 20 px in and keep their top;
  their content moves 20 px left with them and they slide 570. Everything inside one is inset 12 px from the
  panel, the progress bar's inset: text ends on the bar's right edge, the 60 px icon starts on its left edge
  with the heading 10 px after it (456 wide), and text without an icon spans the bar's 526 (cache, volume, Up
  Next; Up Next's two buttons 258 each with their 10 px gap). The select dialog's bottom panel (game OSD)
  keeps its 400 px height, moved up 20 to 660 and 20 px clear of the left and right edges, its content up 20
  and 20 px further in from each side. The scrolling index panel is 75 × 75 at 20, 90, its letter centred,
  sliding 95. The parent folder (`..`, whose sort letter is its ".") and any item without a sort letter show an ellipsis
  (`$VAR[ScrollingLetter]`), so the panel never stands empty and never slides out mid-scroll. The RSS bar floats the same way.
- **Artwork** is rounded with a diffuse mask: `diffuse="common/masks/art-WxH.png"` on the texture, one mask
  per box size (8 px from 100 px up, 4 px below). View images take it as the `mask` param of
  `MediaViewImageNF`/`FO`; the widget image builds its name from its `width` and `height` params. Art drawn
  with `keep` takes the mask on the drawn image, so corners are exact where the image fills its box and oval
  where its aspect differs; art drawn with `scale` needs `scalediffuse="false"` so the mask follows the box
  rather than the scaled image. Full-screen art and backgrounds stay square. Where one control shows art of a
  known other shape, it is split by content so each takes the mask of the shape it is drawn at: the video
  info image is a 2:3 poster (`art-405x600`) or 16:9 (`art-405x228`: episodes, fanart, thumbs without a
  poster); music and PVR info take the square `art-405x405`.
- **Strips on art** (the wall title strip, the watched-status strip, the widget status bar) draw
  `views/OverlayBottomBar.png` with `border="8,0,8,8"`: square on top, and at the bottom the art mask's own
  8 px corners, so they meet the rounded art exactly. Text and badges keep at least 8 px from both ends of a
  strip, clear of the corners, whatever its height. Art that a strip can overlay (`MediaViewImageNF`/`FO`,
  `widget-image`) is drawn `aligny="bottom"`, so its lower edge is the box's and the strip lies on the image.
  A focus zoom on such art pivots where its first frame puts the focused box's bottom on the unfocused
  box's bottom (the widgets' zoom pivots on the image's bottom centre; the 52x and 53x views name the point),
  so the art's lower edge does not jump when focus arrives.
- **Rows of panels** that touch share one panel rather than rounding each: the bookmark and chapter row in
  `VideoOSDBookmarks.xml` draws one `$VAR[MenuOSDPanel]` behind all its items, as wide as the items it holds
  (`VideoOSDBookmarks_coords1`, an image per count on `Container(11).NumItems`, the last from the count that
  fills the row: 5 at 16:9, 7 at 21:9, 3 at 4:3).
- **Colour swatches** use `common/SwatchRounded.png` (16 × 16, 4 px, `border="4"`); the large live preview
  uses `common/PanelSolid.png` (8 px).
- Stretched bars are 9-slice textures (border = half the height), so the ends stay round at any length.
- Radii are the same at every aspect ratio: all four canvases are drawn at the same pixel scale.

---

### Watched-status overlays and pointer

- Six overlay tiers, 12, 16, 20, 24, 32 and 44 px, strokes 1.5 / 2 / 2 / 2 / 3 / 4, each drawn 1:1 and never
  scaled: `media/views/<tier>/Overlay{Resumable,Progress1–7,ProgressWatched}.png`. A view uses the largest
  tier that fits its bar height (13–15 → 12, 16–19 → 16, 20–23 → 20, 24–31 → 24, 32–43 → 32, 44+ → 44),
  centred in the bar on whole pixels. The tier is chosen from the largest of the four aspect leaves.
- `$VAR[StatusOverlay]` is the file name only; the caller supplies the folder. `MediaViewImageNF`/`FO`,
  `MediaViewTitleStripNF`/`FO` and `widgetOverlayBar` take it as the `overlayset` param (default 24), the
  widget presets as `overlaySet` / `rowOverlaySet`; the list views (22 px box → 20) and PVR recordings
  (30 → 24) name their tier in the path.
- The pointer is 32 × 32, the size `Pointer.xml` draws it, with the arrow tip in the top-left corner (the
  click point).
- The PVR status icons (Recording, Timer, Reminder) use the same approach in three tiers, 16, 24 and 32 px
  (`media/pvr/<tier>/`): 30 px boxes draw 24, the TV guide's 18 px box 16, the widget bars `overlayPvrSet` /
  `rowOverlayPvrSet` (a 20 px two-row bar takes 16, 2 px down).
- Calibration textures are exported at the exact size SettingsScreenCalibration draws them (44 × 44 arrows and
  reset, 500 × 500 pixel ratio, 384 × 86 subtitle bar), and stroked heavily enough to read at the 50 % they are
  dimmed to: arrows and reset 5 px (the arrows' mitred tips exactly in their corner, the reset an open 290° arc
  whose head sits on its end), the subtitle bar 14 px and the pixel ratio box 20 px on whole pixels (18.5 put
  every edge on a half pixel), its diagonals running under the frame so no hairline shows where they meet. The
  arrows' line starts in the corner the head points to. They take the icon tokens, `OverlayColorFO` focused
  and `OverlayColorNF` (33 %) not, the same step as every other icon; their labels keep the text tokens.
- A slider nib is drawn at its texture height times the control height over the background texture height,
  with its own proportions: the seek slider's `OSDSliderNibBig` (6 × 36) on a 20 px control over the 20 px
  `OSDSliderBack` draws 1:1, and the control sits 8 px above the progress bar so the nib is centred on it.

## 11. Playback OSD

| Part | Control | Position | Size |
| --- | --- | --- | --- |
| Bar | group | 150, 945 | 1620 × 60 (2260 at 21:9, 1140 at 4:3) |
| Seek | button 100 | 430, 890 | 920 × 20 |
| Transport | grouplist 29 | 20 in bar | 382 × 60, itemgap 20 |
| Options | grouplist 30 | right 8 | 720 × 60, align right |

- Every button is 60 px tall; the row shares one baseline. Transport glyphs sit flush in their boxes: Play,
  Pause, Stop, Record and the channel buttons 36 wide, trick triangles 18 × 26 and skip bars 5 × 26, centred
  on y 30. Everything on the bar keeps a 20 px inset, the progress bar's time labels included: the transport
  grouplist sits 20 px in, the options grouplist 8 px (its 60 px buttons keep their glyphs 12 px inside, so
  the last glyph ends 20 px from the edge; a narrower last glyph, such as Bookmarks, ends a little further
  in). The transport row has itemgap 20 and no spacers, so a hidden button takes its gap with it. The seek
  buttons join edge to edge inside a skip bar and its triangles: with `usecontrolcoords`, Rewind, Tempo down,
  Fast forward and Next sit at left -20, which draws each over the item gap and takes the gap out. Every
  button stays a direct child of the one grouplist, so it navigates them as a single row, into the options row
  and back. Live TV without timeshift is 260 px, with timeshift 382, a video file 214. The player controls and
  the home now-playing row take the same widths and gap; the home row's fullscreen button keeps its 60 px
  options box, its glyph four 6 px corner brackets on Stop's 36 × 36 box. Focus opens on control 5 (play/pause).
- Up to fifteen option buttons, each visible only when it applies; right alignment keeps them flush. An image
  laid over an option button (repeat, masking) sits on the button's slot, counted from the row's right edge 8 px
  in: right 8 + 60 per slot.
- **Optical size in the transport row.** Pause (two 12 × 36 bars, 34 wide) sets the height. Play matches it
  exactly (33 × 36, y 12–48), with no overshoot; Stop is a 36 × 36 square filling its box. In the options row
  a narrow glyph may be up to 6 px narrower than the 36 px live area (Bookmarks is 30 wide), never less.
- One texture per button; focus is tint (`OverlayColorFO` vs `OverlayColorNF`). An active speed toggle
  keeps the focused tint. Record swaps files (`OSDRecordOff` / `OSDRecordOn`) because the shapes differ.
- Opens with a 90 → 100 back-out zoom; options fade in after 200 ms.
- Info panel: 278 tall, 308 when the audio and subtitle rows show (the cover follows the panel). Live TV adds
  the Next strip 14 px below it, at 292, sliding down the same 30 px with the rows, so it never covers them.
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

- **Full-screen** (yes/no, progress, select, keyboard, info, welcome, setting select, the Skin Shortcuts
  management dialog and every other window including `DialogBackgroundImage`): full screen once open, heading
  in the window-title slot with the clock at right, `DialogButtons` centred at y 914 — 66 tall, Font33, auto
  width, 30 px gap, `focus.png`. Font33 is the button default, so a row button sets no `<font>` of its own.
  Opens and closes with the 70 → 100 zoom; while it zooms its background has 8 px corners, which square off
  while the back tween has the zoom past 100% and the corners off screen. Each background layer is drawn
  twice, square (`DialogZoomAnimationSquare`, `DialogCornerFadeSquare` inside the overlay group) and rounded
  (`DialogZoomAnimationRounded`, `DialogCornerFadeRounded`), and the two swap on one frame: 240 ms into the
  300 ms open, and on the first frame of the close. Never crossfade them — two copies at a and 1 − a cover
  only 1 − a(1 − a), 75% halfway, and the window behind flashes through. Every open animation of a pair starts
  at 0 ms: Kodi hides a control until the earliest effect of its WindowOpen animation begins. The rounded copy
  is at alpha 0 once open, and Kodi culls it, so it costs nothing then. Rounded copies: `PanelSolid` for the
  colour, `Background1*Top`, `Background1*Bottom` and `Background2*Round` for the overlay's outer bands, a per-canvas mask
  (`DialogMask*`, via `DialogBackgroundImageTexture`) for the images.
- **Add-on windows** the skin can draw are skinned here rather than left to the add-on's own look: Up Next
  as corner dialogs, and `script-RSS_Editor.xml` (`script.rss.editor`, one window for its feeds and sets
  pages) as a full-screen dialog laid out like the select dialog's text list: heading from label 2 in the
  title slot, `DefaultNetwork` in the 405 × 600 image slot, the list caption (label 4) on the dialogs'
  explanation line above the buttons (centred, Font27, bottom 180, as `DialogVideoInfo_coords2`), the
  58 px list 10 at 750, 192, eleven rows so it ends 34 px above that line, its scrollbar at 690, and Add, Remove, the set button (11), OK and Cancel in
  `DialogButtons`. The add-on drives controls 2, 4, 10, 11, 13, 14, 18 and 19 by id; keep them. OK and
  Cancel are the add-on's: the skin adds no actions to them, as closing from the skin would skip its save.
- **The window below a full-screen dialog fades out** 300 ms after it opens (`WindowFullscreenDialogFadeAnimation`,
  on the 26 windows that carry it), so it isn't drawn while hidden.
- **Panel and corner** (context menu, extended progress, notification): the window stays visible. Context menu
  is a 430 px `MenuOSDColor` panel at 20, 20 sliding in 460 px from the left, rows 390 × 52 at 40;
  `SubMenuAnimation` keeps the list centred on the panel: instantly in the dialogs, over 200 ms in
  the sub-menus, so their rows glide to the new centre when the player controls come or go. The player
  controls (and their spacer) fade in and out over 200 ms rather than sliding across the panel. Corner dialogs stack via `CornerWindowLift*`.
- **Waiting**: blocking = `DimOverlay` + 200 px spinner; with a percentage = progress dialog
  (760 × 20 bar at y 867); background work = corner dialog with the 60 px spinner, never blocking; a
  reloading widget shows the 36 px spinner.
- **The spinner** is the OSMC mark drawn by one travelling stroke, as APNG for a full alpha edge (Kodi
  loads `.apng` from the file system; TexturePacker leaves it out of the bundle). `$VAR[BusySpinner]`
  200 px, `$VAR[BusySpinnerMedium]` 60 px, `$VAR[BusySpinnerSmall]` 36 px: 60 fps, or 30 fps below 512 MB
  (`busy-slow*`), both a 2.9 s loop that runs straight across the path's seam: no blank frames, the stroke
  never shorter than 18 px. Built from the supplied 60 and 30 fps frames; identical frames are merged,
  since Kodi makes a texture per frame.

## 12b. Other windows and list states

- Reuse the library frame (title/folder top left, clock top right, count bottom right, art at 120, list at 750).
  Own layouts only where needed: TV guide (grid 120, 174, 1680 × 606; channel column 450; rows 69; ruler 54;
  54 five-minute blocks; the now line and its shadow cover the programme blocks exactly, from the grid's
  left edge and from 1 px under the ruler to 1 px above the bottom, and the line has round ends inside the
  9-slice's fixed rows, `border="4,61,4,5"`), weather (six 280 px day columns), file manager (two 800 px
  panes).
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

Reuse these includes. Movement (zoom, slide, scroll) runs 200–300 ms; fades have three set exceptions:

- **Widgets fade over 400 ms**, and fade in only after a 400 ms delay (`widgetIndicators`,
  `widgetHeading-content`, the widget group and its selected/deselected state, the weather outlook).
- **The full-screen dialog overlay fades in 100 ms**, and out in 100 ms after a 200 ms delay
  (`DialogBackgroundImage`, and the same group in `script-skinshortcuts.xml`), inside the 300 ms zoom
  it opens and closes with.
- **`OptionsAnimation` fades in 150 ms after 150 ms**, inside its 300 ms zoom.

A new fade outside 200–300 ms joins this list or does not ship.

---

## 14. Looks wrong, isn't

- **FontNN names ≠ sizes.** Fifteen of the eighteen numbered fonts render smaller than their name
  (Font120 and Font50 match; Kodi's own `font13` is 21 px); in the Arial set, seventeen of eighteen. Kept to
  avoid touching every window file. Read the size.
- **Two FO/NF pairs, and one that isn't.** `common/ScrollbarGripNF`/`FO` and
  `common/ScrollbarGripHorizontalNF`/`FO`: the same 6 px nib, but the unfocused one is split round the
  track, since a translucent nib over it would let the track show through; the opaque focused one covers it. `osd/OSDSliderNibNF`
  and `FO`: the same 16 × 16 nib, the unfocused one split round the track for the same reason.
- **One track with a baked fade.** `osd/OSDProgressBack` carries 30 % in its alpha, as it always has, under
  an `OverlayColorNF` tint, so the track sits well below the fill.
- **Ink at the canvas edge.** The OSDTrick slices run edge to edge so the stacked transport row reads as
  one control; the calibration corner markers sit in their corner; the pointer's click arcs reach the top edge; the bars and scrollbar
  parts run to the canvas edge along their length, so they join seamlessly when drawn 9-slice. The 2 px clearance applies to icons, not to these.
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
- [ ] Textures white-in-alpha, authored at the exact drawn size from the SVG originals, bundle repacked
- [ ] Icons on their tier grid (stroke, live area, 16/4/2 px corners, badge position)
- [ ] Visible panel corners and art 8 px, small art, swatches and elements 4 px, thin bars round at their outer ends; background textures plain
- [ ] Motion from the shared animation includes
- [ ] Survives every visual setting listed in §12
- [ ] Handles empty, loading, parent-folder and long-title states
- [ ] Fits in the longest translation; button rows inside the safe area
