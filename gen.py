import requests
from io import BytesIO
from PIL import Image
import base64

r = requests.get('https://i.scdn.co/image/ab67616d0000b2739e1cfc756886ac782e363d79')
img = Image.open(BytesIO(r.content))
img = img.resize((360, 360), Image.LANCZOS)
buf = BytesIO()
img.save(buf, 'JPEG', quality=85)
b64 = base64.b64encode(buf.getvalue()).decode()

bars = ''
for i in range(35):
    x = 30 + i * 10
    h = 5 + (i * 13 + i * i * 2 + 7) % 16
    op = 0.3 + (abs(17 - i) * 0.035)
    if op > 1: op = 1
    bars += f'  <rect x="{x}" y="{112 - h}" width="5" height="{h}" rx="2.5" fill="#1DB954" opacity="{op:.2f}"/>\n'

svg = f'''<svg width="400" height="520" viewBox="0 0 400 520" xmlns="http://www.w3.org/2000/svg" aria-labelledby="cardTitle" role="img">
  <title id="cardTitle">Now playing on Spotify</title>
  <defs>
    <clipPath id="cc"><rect x="20" y="145" width="360" height="360" rx="12"/></clipPath>
  </defs>
  <rect width="400" height="520" rx="16" fill="#121212"/>
  <text x="200" y="28" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" font-weight="400" fill="#a0a0a0" letter-spacing="1.5">NOW PLAYING ON</text>
  <text x="200" y="45" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#1DB954">SPOTIFY</text>
  <text x="200" y="72" text-anchor="middle" font-family="Arial,sans-serif" font-size="24" font-weight="bold" fill="#ffffff">Let It Happen</text>
  <text x="200" y="96" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="400" fill="#a0a0a0">Tame Impala</text>
{bars}
  <image href="data:image/jpeg;base64,{b64}" x="20" y="145" width="360" height="360" clip-path="url(#cc)"/>
  <a href="https://open.spotify.com/track/7uLz3wJ1fVwL7JfScdMX6R" target="_blank">
    <rect x="0" y="0" width="400" height="520" fill="transparent"/>
  </a>
</svg>'''

with open('dist/spotify.svg', 'w', encoding='utf-8') as f:
    f.write(svg)
with open('dist/spotify-novatorem.svg', 'w', encoding='utf-8') as f:
    f.write(svg)
print(f'Done: {len(svg)} chars')
