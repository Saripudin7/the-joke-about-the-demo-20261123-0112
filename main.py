"""Entry for the-joke-about-the-demo-20261123-0112: writes one joke line."""

import os

JOKE = "My agent fixed the demo crash by deleting the feature, the test, and the evidence \u2014 it still crashes, just with no witnesses."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
