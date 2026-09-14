#!/usr/bin/env python3
"""Render an icon vector to the PNG the skin ships.

    render-icons.py icons/DefaultTVShows.svg media/DefaultTVShows.png 405 405

The size is the one the largest control on screen draws the icon at, which is why it
differs per icon. Output is 8-bit grey + alpha, white throughout, so the packer stores a
single channel and the skin's colordiffuse carries the colour.

Needs chromium (any headless build) and nothing else. Set CHROMIUM to point at it.
"""
import os, re, struct, subprocess, sys, tempfile, zlib

CHROMIUM = os.environ.get("CHROMIUM", "chromium")


def render(svg_path, width, height, out_png):
    svg = open(svg_path, encoding="utf-8").read()
    svg = svg.replace('fill="#000000"', 'fill="#ffffff"')
    svg = re.sub(r"^.*?(?=<svg)", "", svg, flags=re.S)
    svg = re.sub(r"<svg([^>]*)>",
                 lambda m: "<svg" + re.sub(r'\s(width|height)="[^"]*"', "", m.group(1)) + ">",
                 svg, count=1)
    html = ("<!doctype html><meta charset=\"utf-8\"><style>"
            "html,body{margin:0;padding:0;background:transparent;overflow:hidden}"
            "svg{display:block;width:100vw;height:100vh}</style>" + svg)
    with tempfile.TemporaryDirectory() as tmp:
        page = os.path.join(tmp, "icon.html")
        shot = os.path.join(tmp, "icon.png")
        open(page, "w", encoding="utf-8").write(html)
        subprocess.run([CHROMIUM, "--headless", "--no-sandbox", "--disable-gpu",
                        "--hide-scrollbars", "--force-device-scale-factor=1",
                        "--default-background-color=00000000", "--screenshot=" + shot,
                        "--window-size=%d,%d" % (width, height), "file://" + page],
                       check=True, capture_output=True)
        write_grey_alpha(out_png, alpha_of(shot, width, height), width, height)


def alpha_of(png, width, height):
    """Pull the alpha channel out of chromium's RGBA screenshot."""
    data = open(png, "rb").read()
    pos, idat, ctype = 8, b"", None
    while pos < len(data):
        length = struct.unpack(">I", data[pos:pos + 4])[0]
        kind = data[pos + 4:pos + 8]
        if kind == b"IHDR":
            w, h, _, ctype = struct.unpack(">IIBB", data[pos + 8:pos + 18])
            if (w, h) != (width, height):
                raise SystemExit("chromium rendered %dx%d, wanted %dx%d" % (w, h, width, height))
        elif kind == b"IDAT":
            idat += data[pos + 8:pos + 8 + length]
        pos += 12 + length
    channels = {0: 1, 2: 3, 4: 2, 6: 4}[ctype]
    raw, stride, rows, prev, i = zlib.decompress(idat), width * channels, [], bytearray(width * channels), 0
    for _ in range(height):
        filt, line, i = raw[i], bytearray(raw[i + 1:i + 1 + stride]), i + 1 + stride
        for x in range(stride):
            a = line[x - channels] if x >= channels else 0
            b = prev[x]
            c = prev[x - channels] if x >= channels else 0
            if filt == 1: line[x] = (line[x] + a) & 255
            elif filt == 2: line[x] = (line[x] + b) & 255
            elif filt == 3: line[x] = (line[x] + (a + b) // 2) & 255
            elif filt == 4:
                p = a + b - c
                pa, pb, pc = abs(p - a), abs(p - b), abs(p - c)
                line[x] = (line[x] + (a if pa <= pb and pa <= pc else b if pb <= pc else c)) & 255
        out = bytearray()
        for x in range(width):
            out += bytes((255, line[x * channels + channels - 1]))
        rows.append(bytes(out))
        prev = line
    return rows


def write_grey_alpha(path, rows, width, height):
    def chunk(kind, payload):
        body = kind + payload
        return struct.pack(">I", len(payload)) + body + struct.pack(">I", zlib.crc32(body) & 0xffffffff)
    raw = b"".join(b"\x00" + row for row in rows)
    open(path, "wb").write(b"\x89PNG\r\n\x1a\n"
                           + chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 4, 0, 0, 0))
                           + chunk(b"IDAT", zlib.compress(raw, 9))
                           + chunk(b"IEND", b""))


if __name__ == "__main__":
    if len(sys.argv) != 5:
        raise SystemExit(__doc__)
    render(sys.argv[1], int(sys.argv[3]), int(sys.argv[4]), sys.argv[2])
