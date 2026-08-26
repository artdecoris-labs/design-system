# Storefront imagery — what to supply

21 images. Drop them into `assets/` using the **name** column (any of `.webp`, `.jpg`, `.png`).
A GitHub repo works too — point me at it and I will copy them in.

| Name | Where it appears | Recommended size | Live source |
| --- | --- | --- | --- |
| `hero-interior` | Home hero — interior, full-bleed | 1600×900 or larger, landscape | `https://www.artdecoris.com/web/image/8244-0b2df0eb/ARTDECORIS-37.webp` |
| `custom-room` | Custom-made editorial band | 1600×900, landscape | `https://www.artdecoris.com/web/image/7221-d715be84/358-DSC02192-min.jpg` |
| `collab-deferla` | De Ferla × B.R.A.S.S. split block | 1200×825, landscape | `https://www.artdecoris.com/web/image/8092-e19f4aed/Deferla%20x%20Brass-6.webp` |
| `banner-wallart` | Collection page banner | 1600×700, landscape | `https://www.artdecoris.com/web/image/8802-f0c5ec98/56.webp` |
| `cat-wallart` | Category tile — Wall art | 900×1200, portrait 3:4 | `https://www.artdecoris.com/web/image/8802-f0c5ec98/56.webp` |
| `cat-candles` | Category tile — Candles & diffusers | 900×1200, portrait 3:4 | `https://www.artdecoris.com/web/image/8801-1f1fd0be/52.webp` |
| `cat-outdoor` | Category tile — Outdoor deco | 900×1200, portrait 3:4 | `https://www.artdecoris.com/web/image/8804-81d10168/53.webp` |
| `artist-anne` | Artist card — Anne Mondy | 800×1000, portrait 4:5 | `https://www.artdecoris.com/web/image/8100-bafd4117/6.webp` |
| `artist-brass` | Artist card — B.R.A.S.S. | 800×1000, portrait 4:5 | `https://www.artdecoris.com/web/image/8104-240d8339/7.webp` |
| `artist-juan` | Artist card — Juan de Lascurain | 800×1000, portrait 4:5 | `https://www.artdecoris.com/web/image/8264-4b330eb6/images.webp` |
| `prod-bici` | Product — Wall Decoration Bici | 900×900, square | `https://www.artdecoris.com/web/image/product.template/166/image_1024?unique=2c7de7f` |
| `prod-flowers` | Product — Wall Decoration Flowers | 900×900, square | `https://www.artdecoris.com/web/image/product.template/165/image_1024` |
| `prod-ojitos` | Product — Wall Decoration Ojitos | 900×900, square | `https://www.artdecoris.com/web/image/product.template/168/image_1024` |
| `prod-hearts` | Product — Wall Decoration Hearts | 900×900, square | `https://www.artdecoris.com/web/image/product.template/164/image_1024` |
| `prod-bici-xl` | Product — Plexi Edition Bici XL | 900×900, square | `https://www.artdecoris.com/web/image/product.image/526/image_1024/C%20005c%20Plexi%20Bike%20XL.webp?unique=0b831b3` |
| `prod-frame` | Product — Framed Edition Vertical | 900×900, square | `https://www.artdecoris.com/web/image/product.image/208/image_1024/Frame%20vertical%20open-min-min.webp?unique=0b831b3` |
| `gallery-2` | PDP gallery 2 — Bici XL view | 900×900, square | `https://www.artdecoris.com/web/image/product.image/526/image_1024/C%20005c%20Plexi%20Bike%20XL.webp?unique=0b831b3` |
| `gallery-3` | PDP gallery 3 — Bici triptych | 900×900, square | `https://www.artdecoris.com/web/image/product.image/134/image_1024/C%20005d%20Plexi%20Bike%203x-min.webp?unique=0b831b3` |
| `gallery-4` | PDP gallery 4 — reverse / mount | 900×900, square | `https://www.artdecoris.com/web/image/product.image/222/image_1024/C%20014%20achterkant%20small.webp?unique=0b831b3` |
| `mega-shop` | Mega-menu promo — Shop | 800×600, landscape 4:3 | `https://www.artdecoris.com/web/image/8801-1f1fd0be/52.webp` |
| `mega-artists` | Mega-menu promo — Artists | 800×600, landscape 4:3 | `https://www.artdecoris.com/web/image/8092-e19f4aed/Deferla%20x%20Brass-6.webp` |

## Fastest route

```bash
python3 assets/download_images.py          # standard library only
python3 assets/download_images.py --force  # re-download over existing files
```

Skips anything already in `assets/`, picks the extension from the response type, and reports per-file failures at the end. Shell equivalent: `bash assets/download-images.sh`. Machine-readable list: `assets/image-manifest.json`.

## Notes

- Four names reuse the same source photo today (`cat-wallart` / `banner-wallart`, `mega-shop` / `cat-candles`, `mega-artists` / `collab-deferla`, `gallery-2` / `prod-bici-xl`). Replace any of them with a better-cropped shot at the recommended aspect ratio when you have one.
- Product shots should be square on a neutral background; lifestyle shots full-bleed, warm daylight, art in situ.
- Nothing in the code needs to change once the files land — the storefront prefers a local file over the live URL automatically.

---

## Status — 2026-08-26

All 21 placeholders replaced with the real imagery pulled from the live Odoo shop
(<https://www.artdecoris.com>) via the source URLs above. `logo.png` was already real.

`custom-room` is served as JPEG despite the `.jpg` source being requested into a `.webp`
name; it is stored as `custom-room.jpg` to match its actual content.

**Four of them do not meet the recommended spec and should be re-shot or re-exported
before launch:**

| Name | Got | Wanted | Problem |
| --- | --- | --- | --- |
| `artist-juan` | 221×228 | 800×1000 | Far too small — a thumbnail, not a portrait. Unusable at card size. |
| `hero-interior` | 1024×671 | 1600×900+ | Will soften on wide displays; it is the first thing on the home page. |
| `cat-wallart`, `cat-candles`, `cat-outdoor` | 720×720 | 900×1200 (3:4) | Square source into a portrait tile means a hard vertical crop. |
| `banner-wallart` | 720×720 | 1600×700 | Square into a wide banner — severe crop. |

Odoo serves resized derivatives from `/web/image/...`. Larger originals may exist in the
Odoo backend; pulling them through the Admin API during the catalog migration will
generally give better source files than the public web derivatives used here.
