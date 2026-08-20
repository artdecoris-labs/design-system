#!/usr/bin/env bash
# Download the ArtDecoris storefront imagery into assets/.
# Run from the project root:  bash assets/download-images.sh
set -euo pipefail
mkdir -p assets

curl -fL --retry 2 -o "assets/hero-interior.webp" \
  "https://www.artdecoris.com/web/image/8244-0b2df0eb/ARTDECORIS-37.webp"
curl -fL --retry 2 -o "assets/custom-room.webp" \
  "https://www.artdecoris.com/web/image/7221-d715be84/358-DSC02192-min.jpg"
curl -fL --retry 2 -o "assets/collab-deferla.webp" \
  "https://www.artdecoris.com/web/image/8092-e19f4aed/Deferla%20x%20Brass-6.webp"
curl -fL --retry 2 -o "assets/banner-wallart.webp" \
  "https://www.artdecoris.com/web/image/8802-f0c5ec98/56.webp"
curl -fL --retry 2 -o "assets/cat-wallart.webp" \
  "https://www.artdecoris.com/web/image/8802-f0c5ec98/56.webp"
curl -fL --retry 2 -o "assets/cat-candles.webp" \
  "https://www.artdecoris.com/web/image/8801-1f1fd0be/52.webp"
curl -fL --retry 2 -o "assets/cat-outdoor.webp" \
  "https://www.artdecoris.com/web/image/8804-81d10168/53.webp"
curl -fL --retry 2 -o "assets/artist-anne.webp" \
  "https://www.artdecoris.com/web/image/8100-bafd4117/6.webp"
curl -fL --retry 2 -o "assets/artist-brass.webp" \
  "https://www.artdecoris.com/web/image/8104-240d8339/7.webp"
curl -fL --retry 2 -o "assets/artist-juan.webp" \
  "https://www.artdecoris.com/web/image/8264-4b330eb6/images.webp"
curl -fL --retry 2 -o "assets/prod-bici.webp" \
  "https://www.artdecoris.com/web/image/product.template/166/image_1024?unique=2c7de7f"
curl -fL --retry 2 -o "assets/prod-flowers.webp" \
  "https://www.artdecoris.com/web/image/product.template/165/image_1024"
curl -fL --retry 2 -o "assets/prod-ojitos.webp" \
  "https://www.artdecoris.com/web/image/product.template/168/image_1024"
curl -fL --retry 2 -o "assets/prod-hearts.webp" \
  "https://www.artdecoris.com/web/image/product.template/164/image_1024"
curl -fL --retry 2 -o "assets/prod-bici-xl.webp" \
  "https://www.artdecoris.com/web/image/product.image/526/image_1024/C%20005c%20Plexi%20Bike%20XL.webp?unique=0b831b3"
curl -fL --retry 2 -o "assets/prod-frame.webp" \
  "https://www.artdecoris.com/web/image/product.image/208/image_1024/Frame%20vertical%20open-min-min.webp?unique=0b831b3"
curl -fL --retry 2 -o "assets/gallery-2.webp" \
  "https://www.artdecoris.com/web/image/product.image/526/image_1024/C%20005c%20Plexi%20Bike%20XL.webp?unique=0b831b3"
curl -fL --retry 2 -o "assets/gallery-3.webp" \
  "https://www.artdecoris.com/web/image/product.image/134/image_1024/C%20005d%20Plexi%20Bike%203x-min.webp?unique=0b831b3"
curl -fL --retry 2 -o "assets/gallery-4.webp" \
  "https://www.artdecoris.com/web/image/product.image/222/image_1024/C%20014%20achterkant%20small.webp?unique=0b831b3"
curl -fL --retry 2 -o "assets/mega-shop.webp" \
  "https://www.artdecoris.com/web/image/8801-1f1fd0be/52.webp"
curl -fL --retry 2 -o "assets/mega-artists.webp" \
  "https://www.artdecoris.com/web/image/8092-e19f4aed/Deferla%20x%20Brass-6.webp"

echo "Done. 21 files in assets/ — re-publish the design."
