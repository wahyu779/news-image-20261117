#!/usr/bin/env python3
"""Render page.html into entry.png with a headless Chromium screenshot.

This is the build step for the Daily World newspaper front page. It only
runs locally while building the entry; the entry program itself (main.ts)
just copies the finished entry.png. Rendering is deterministic: the same
page and the same local assets always produce the same bytes.

Usage: python3 render.py  (writes entry.png next to this file)
"""

import hashlib
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PAGE = os.path.join(HERE, "page.html")
OUT = os.path.join(HERE, "entry.png")

# Chromium binaries known on this machine, in order of preference.
# (The Meta Chromium at /opt/meta-chromium/chrome refuses to start
# headless here — it wants a Hatch WebGL domain policy — so the
# Playwright headless shell is the working renderer.)
CHROMIUMS = [
    os.path.expanduser(
        "~/.cache/ms-playwright/chromium_headless_shell-1187/chrome-linux/headless_shell"),
    os.path.expanduser(
        "~/.cache/ms-playwright/chromium-1187/chrome-linux/chrome"),
    "/opt/meta-chromium/chrome",
]


def find_chromium():
    for path in CHROMIUMS:
        if os.path.isfile(path) and os.access(path, os.X_OK):
            return path
    return None


def main():
    chrome = find_chromium()
    if chrome is None:
        print("no Chromium binary found", file=sys.stderr)
        return 1
    if not os.path.isfile(PAGE):
        print("page.html missing:", PAGE, file=sys.stderr)
        return 1
    if os.path.exists(OUT):
        os.remove(OUT)
    cmd = [
        chrome,
        "--headless",
        "--no-sandbox",
        "--disable-gpu",
        "--hide-scrollbars",
        "--force-device-scale-factor=1",
        "--window-size=1024,1024",
        "--virtual-time-budget=5000",
        "--screenshot=" + OUT,
        "file://" + PAGE,
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print("chromium failed:", result.stderr, file=sys.stderr)
        return 1
    if not os.path.isfile(OUT):
        print("entry.png was not produced", file=sys.stderr)
        return 1
    from PIL import Image

    with Image.open(OUT) as im:
        print("entry.png:", im.size, im.mode)
        if im.size != (1024, 1024):
            print("unexpected size, expected 1024x1024", file=sys.stderr)
            return 1
    size = os.path.getsize(OUT)
    digest = hashlib.sha256(open(OUT, "rb").read()).hexdigest()
    print("bytes:", size)
    print("sha256:", digest)
    if size > 1024 * 1024:
        print("over the 1 MiB entry cap", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
