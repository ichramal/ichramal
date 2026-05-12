import requests
from io import BytesIO
from PIL import Image
import base64

r = requests.get('https://i.scdn.co/image/ab67616d0000b2739e1cfc756886ac782e363d79')
img = Image.open(BytesIO(r.content))

img_big = img.resize((320, 320), Image.LANCZOS)
buf = BytesIO()
img_big.save(buf, 'JPEG', quality=90)
b64 = base64.b64encode(buf.getvalue()).decode()

img_small = img.resize((40, 40), Image.LANCZOS)
buf_small = BytesIO()
img_small.save(buf_small, 'JPEG', quality=60)
b64_blur = base64.b64encode(buf_small.getvalue()).decode()

svg = f'''<svg width="400" height="560" viewBox="0 0 400 560" xmlns="http://www.w3.org/2000/svg" aria-labelledby="cardTitle" role="img">
  <title id="cardTitle">Now playing on Spotify</title>
  <defs>
    <filter id="blur"><feGaussianBlur stdDeviation="40"/></filter>
    <clipPath id="cc"><rect x="40" y="100" width="320" height="320" rx="16"/></clipPath>
  </defs>
  <image href="data:image/jpeg;base64,{b64_blur}" x="0" y="0" width="400" height="560" preserveAspectRatio="xMidYMid slice" filter="url(#blur)"/>
  <rect x="0" y="0" width="400" height="560" fill="#121212" opacity="0.45"/>
  <circle cx="80" cy="35" r="14" fill="#1DB954"/>
  <polygon points="75,28 75,42 88,35" fill="#121212"/>
  <text x="100" y="40" font-family="Arial,sans-serif" font-size="16" font-weight="bold" fill="#ffffff">Spotify</text>
  <image href="data:image/jpeg;base64,{b64}" x="40" y="100" width="320" height="320" clip-path="url(#cc)"/>
  <text x="200" y="460" text-anchor="middle" font-family="Arial,sans-serif" font-size="26" font-weight="bold" fill="#ffffff">Let It Happen</text>
  <text x="200" y="485" text-anchor="middle" font-family="Arial,sans-serif" font-size="15" font-weight="400" fill="#b3b3b3">Tame Impala</text>

  <rect x="110" y="510" width="180" height="36" rx="18" fill="#1DB954"/>
  <polygon points="148,521 148,535 162,528" fill="#ffffff"/>
  <text x="172" y="533" font-family="Arial,sans-serif" font-size="12" font-weight="bold" fill="#ffffff">PLAY ON SPOTIFY</text>

  <a href="https://open.spotify.com/track/7uLz3wJ1fVwL7JfScdMX6R" target="_blank">
    <rect x="0" y="0" width="400" height="560" fill="transparent"/>
  </a>
</svg>'''

with open('dist/spotify.svg', 'w', encoding='utf-8') as f:
    f.write(svg)
with open('dist/spotify-novatorem.svg', 'w', encoding='utf-8') as f:
    f.write(svg)
print(f'Done: {len(svg)} chars')
