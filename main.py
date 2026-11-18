# main.py — news-image-20261118 entry program.
# Copies the repository's front-page image (entry.png) to the output directory.
# Python 3.13 stdlib only, no network, no randomness, no clock: running it
# twice writes identical bytes.
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUT_DIR, exist_ok=True)
shutil.copyfile(os.path.join(HERE, "entry.png"),
                os.path.join(OUT_DIR, "entry.png"))
