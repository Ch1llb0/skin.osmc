# Icon sources

The vector originals for the icons in `media/` that this skin draws itself. Kodi never reads
this folder — it reads the PNGs — but a PNG cannot be redrawn once a control grows, and these
were redrawn from scratch the first time that happened.

Each SVG is rendered to the size the largest control on screen actually draws it at, which is
not a round number and is not the same for every icon: an icon that never leaves a 256 slot is
not worth 400 pixels of texture memory.

To re-render one after editing it, or after a coordinate change moves a control to a new size:

```sh
# needs chromium and potrace; the renderer is a headless screenshot at the exact pixel size
python3 .github/scripts/render-icons.py icons/DefaultTVShows.svg media/DefaultTVShows.png 405 405
```

Then rebuild `media/Textures.xbt` with TexturePacker 3 (`-dupecheck`), or Kodi keeps serving the
copy inside the bundle.
