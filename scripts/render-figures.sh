#!/usr/bin/env bash
# Render assets/figures/*.svg to PNG (same size as the SVG viewBox) with headless Chromium + ImageMagick crop.
set -euo pipefail
CH="${CHROME:-/opt/pw-browsers/chromium-1194/chrome-linux/chrome}"
cd "$(dirname "$0")/../assets/figures"
for svg in *.svg; do
  n="${svg%.svg}"
  w=$(grep -o 'viewBox="[^"]*"' "$svg" | head -1 | awk '{print $3}'); h=$(grep -o 'viewBox="[^"]*"' "$svg" | head -1 | awk '{print $4}' | tr -d '"')
  printf '<html><body style="margin:0;background:#fff"><img src="file://%s/%s" width="%s" height="%s" style="display:block"></body></html>' "$PWD" "$svg" "$w" "$h" > "/tmp/render_$n.html"
  "$CH" --headless --no-sandbox --disable-gpu --hide-scrollbars --force-device-scale-factor=1 --screenshot="/tmp/$n.full.png" --window-size="$w,$((h+150))" "file:///tmp/render_$n.html" >/dev/null 2>&1
  convert "/tmp/$n.full.png" -crop "${w}x${h}+0+0" +repage "$n.png"
  echo "$n.png ${w}x${h}"
done
