#!/usr/bin/env python3
"""Download the ArtDecoris storefront imagery into assets/.

Usage (from the project root):
    python3 assets/download_images.py
    python3 assets/download_images.py --dir assets --force

Reads assets/image-manifest.json when present, otherwise falls back to the
list embedded below. Standard library only — no pip install needed.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

MANIFEST = Path(__file__).with_name("image-manifest.json")

FALLBACK_IMAGES = [
    {"name": "hero-interior", "source": "https://www.artdecoris.com/web/image/8244-0b2df0eb/ARTDECORIS-37.webp"},
    {"name": "custom-room", "source": "https://www.artdecoris.com/web/image/7221-d715be84/358-DSC02192-min.jpg"},
    {"name": "collab-deferla", "source": "https://www.artdecoris.com/web/image/8092-e19f4aed/Deferla%20x%20Brass-6.webp"},
    {"name": "banner-wallart", "source": "https://www.artdecoris.com/web/image/8802-f0c5ec98/56.webp"},
    {"name": "cat-wallart", "source": "https://www.artdecoris.com/web/image/8802-f0c5ec98/56.webp"},
    {"name": "cat-candles", "source": "https://www.artdecoris.com/web/image/8801-1f1fd0be/52.webp"},
    {"name": "cat-outdoor", "source": "https://www.artdecoris.com/web/image/8804-81d10168/53.webp"},
    {"name": "artist-anne", "source": "https://www.artdecoris.com/web/image/8100-bafd4117/6.webp"},
    {"name": "artist-brass", "source": "https://www.artdecoris.com/web/image/8104-240d8339/7.webp"},
    {"name": "artist-juan", "source": "https://www.artdecoris.com/web/image/8264-4b330eb6/images.webp"},
    {"name": "prod-bici", "source": "https://www.artdecoris.com/web/image/product.template/166/image_1024?unique=2c7de7f"},
    {"name": "prod-flowers", "source": "https://www.artdecoris.com/web/image/product.template/165/image_1024"},
    {"name": "prod-ojitos", "source": "https://www.artdecoris.com/web/image/product.template/168/image_1024"},
    {"name": "prod-hearts", "source": "https://www.artdecoris.com/web/image/product.template/164/image_1024"},
    {"name": "prod-bici-xl", "source": "https://www.artdecoris.com/web/image/product.image/526/image_1024/C%20005c%20Plexi%20Bike%20XL.webp?unique=0b831b3"},
    {"name": "prod-frame", "source": "https://www.artdecoris.com/web/image/product.image/208/image_1024/Frame%20vertical%20open-min-min.webp?unique=0b831b3"},
    {"name": "gallery-2", "source": "https://www.artdecoris.com/web/image/product.image/526/image_1024/C%20005c%20Plexi%20Bike%20XL.webp?unique=0b831b3"},
    {"name": "gallery-3", "source": "https://www.artdecoris.com/web/image/product.image/134/image_1024/C%20005d%20Plexi%20Bike%203x-min.webp?unique=0b831b3"},
    {"name": "gallery-4", "source": "https://www.artdecoris.com/web/image/product.image/222/image_1024/C%20014%20achterkant%20small.webp?unique=0b831b3"},
    {"name": "mega-shop", "source": "https://www.artdecoris.com/web/image/8801-1f1fd0be/52.webp"},
    {"name": "mega-artists", "source": "https://www.artdecoris.com/web/image/8092-e19f4aed/Deferla%20x%20Brass-6.webp"},
]

EXTENSIONS = (".webp", ".jpg", ".jpeg", ".png")
USER_AGENT = "Mozilla/5.0 (ArtDecoris asset sync)"


def load_images() -> list[dict]:
    if MANIFEST.exists():
        data = json.loads(MANIFEST.read_text(encoding="utf-8"))
        return data["images"]
    return FALLBACK_IMAGES


def already_present(target_dir: Path, name: str) -> Path | None:
    for ext in EXTENSIONS:
        candidate = target_dir / f"{name}{ext}"
        if candidate.exists() and candidate.stat().st_size > 0:
            return candidate
    return None


def extension_for(url: str, content_type: str) -> str:
    if "webp" in content_type:
        return ".webp"
    if "png" in content_type:
        return ".png"
    if "jpeg" in content_type or "jpg" in content_type:
        return ".jpg"
    for ext in EXTENSIONS:
        if ext in url.lower():
            return ext
    return ".webp"


def fetch(url: str, timeout: float) -> tuple[bytes, str]:
    request = Request(url, headers={"User-Agent": USER_AGENT})
    with urlopen(request, timeout=timeout) as response:
        return response.read(), response.headers.get("Content-Type", "")


def main() -> int:
    parser = argparse.ArgumentParser(description="Fetch ArtDecoris storefront imagery.")
    parser.add_argument("--dir", default="assets", help="destination directory (default: assets)")
    parser.add_argument("--force", action="store_true", help="re-download files that already exist")
    parser.add_argument("--timeout", type=float, default=30.0, help="per-request timeout in seconds")
    args = parser.parse_args()

    target_dir = Path(args.dir)
    target_dir.mkdir(parents=True, exist_ok=True)

    images = load_images()
    saved, skipped, failed = 0, 0, []

    for image in images:
        name, url = image["name"], image["source"]

        existing = already_present(target_dir, name)
        if existing and not args.force:
            print(f"skip   {name:16s} already present as {existing.name}")
            skipped += 1
            continue

        try:
            payload, content_type = fetch(url, args.timeout)
        except (HTTPError, URLError, TimeoutError) as error:
            print(f"FAIL   {name:16s} {error}", file=sys.stderr)
            failed.append(name)
            continue

        if not payload:
            print(f"FAIL   {name:16s} empty response", file=sys.stderr)
            failed.append(name)
            continue

        destination = target_dir / f"{name}{extension_for(url, content_type)}"
        destination.write_bytes(payload)
        print(f"saved  {name:16s} -> {destination}  ({len(payload) / 1024:.0f} kB)")
        saved += 1

    print(f"\n{saved} saved, {skipped} skipped, {len(failed)} failed")
    if failed:
        print("failed: " + ", ".join(failed), file=sys.stderr)
        print("Export those from the Odoo back-office and drop them into assets/ by name.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
