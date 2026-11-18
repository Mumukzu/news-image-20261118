# main.py — news-image-20261118 entry program (v3).
# Copies the repository's front-page image (entry.png) to the output directory.
# Python 3.13 stdlib only, no network, no randomness, no clock: running it
# twice writes identical bytes. v3 image: 60 stories, 6 illustrated leads,
# 48 briefs with icons, SPORT & MARKETS panel, world map with 28 city markers.
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
SRC = os.path.join(HERE, "entry.png")

with open(SRC, "rb") as f:
    magic = f.read(8)
assert magic == b"\x89PNG\r\n\x1a\n", "entry.png is not a PNG file"

os.makedirs(OUT_DIR, exist_ok=True)
dst = os.path.join(OUT_DIR, "entry.png")
shutil.copyfile(SRC, dst)
# Deterministic by construction: same input bytes, same output bytes.
print("entry.png copied:", os.path.getsize(SRC), "bytes ->", dst)
