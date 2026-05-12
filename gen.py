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

# Generate 30 bars from left to right across the card
bars = ''
for i in range(30):
    x = 40 + i * 11
    h = 5 + (i * 7 + i * i * 3 + 13) % 15
    op = 0.3 + (i % 7) * 0.1
    bars += f'  <rect x="{x}" y="{110 - h}" width="4" height="{h}" rx="2" fill="#1DB954" opacity="{op:.1f}"/>\n'

svg_template = f'''<svg width="400" height="500" viewBox="0 0 400 500" xmlns="http://www.w3.org/2000/svg" aria-labelledby="cardTitle" role="img">
  <title id="cardTitle">Now playing on Spotify</title>
  <defs>
    <clipPath id="cc"><rect x="20" y="135" width="360" height="360" rx="12"/></clipPath>
  </defs>
  <rect width="400" height="500" rx="16" fill="#181818"/>
  <text x="185" y="30" text-anchor="end" font-family="Arial,sans-serif" font-size="12" font-weight="400" fill="#a0a0a0" letter-spacing="1">NOW PLAYING ON</text>
  <text x="198" y="30" text-anchor="start" font-family="Arial,sans-serif" font-size="12" font-weight="bold" fill="#1DB954">SPOTIFY</text>
  <text x="200" y="65" text-anchor="middle" font-family="Arial,sans-serif" font-size="24" font-weight="bold" fill="#ffffff">Let It Happen</text>
  <text x="200" y="90" text-anchor="middle" font-family="Arial,sans-serif" font-size="15" font-weight="400" fill="#a0a0a0">Tame Impala</text>
{bars}  <image href="data:image/jpeg;base64,{b64}" x="20" y="135" width="360" height="360" clip-path="url(#cc)"/>
  <a href="https://open.spotify.com/track/7uLz3wJ1fVwL7JfScdMX6R" target="_blank">
    <rect x="0" y="0" width="400" height="500" fill="transparent"/>
  </a>
</svg>'''

with open('dist/spotify.svg', 'w', encoding='utf-8') as f:
    f.write(svg_template)
with open('dist/spotify-novatorem.svg', 'w', encoding='utf-8') as f:
    f.write(svg_template)
print(f'Done: {len(svg_template)} chars, b64: {len(b64)}')
