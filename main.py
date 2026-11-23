"""News-image entry for make.fun news-image-20261122.

Writes the image stored beside this file to /output/entry.png.
The image is kept base64-encoded in entry.png.b64 because the
upload path is text-only; decoding it gives the exact image bytes.
Standard library only, no network, deterministic: the same bytes
every run, because it decodes the same stored data.
"""

import base64
import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png.b64"


def main() -> None:
    data = base64.b64decode(SRC.read_text(encoding="ascii"))
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.png").write_bytes(data)


if __name__ == "__main__":
    main()
