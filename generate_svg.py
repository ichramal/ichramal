import requests
from io import BytesIO
from PIL import Image
import base64

r = requests.get('https://i.scdn.co/image/ab67616d0000b2739e1cfc756886ac782e363d79')
img = Image.open(BytesIO(r.content))

img_r = img.resize((250, 250), Image.LANCZOS)
buf = BytesIO()
img_r.save(buf, 'JPEG', quality=85)
b64 = base64.b64encode(buf.getvalue()).decode()

svg = f'''<svg width="400" height="420" viewBox="0 0 400 420" xmlns="http://www.w3.org/2000/svg" aria-labelledby="cardTitle" role="img">
  <title id="cardTitle">Now playing on Spotify</title>
  <defs>
    <clipPath id="cc"><rect x="75" y="145" width="250" height="250" rx="10"/></clipPath>
  </defs>

  <rect width="400" height="420" rx="14" fill="#181818"/>

  <text x="72" y="28" font-family="CircularSp, spotify-circular, -apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="400" fill="#a0a0a0" letter-spacing="1">NOW PLAYING ON</text>
  <text x="152" y="28" font-family="CircularSp, spotify-circular, -apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="bold" fill="#1DB954" letter-spacing="0">SPOTIFY</text>

  <text x="50" y="60" font-family="CircularSp, spotify-circular, -apple-system, BlinkMacSystemFont, sans-serif" font-size="22" font-weight="bold" fill="#ffffff">Let It Happen</text>

  <text x="50" y="83" font-family="CircularSp, spotify-circular, -apple-system, BlinkMacSystemFont, sans-serif" font-size="14" font-weight="400" fill="#a0a0a0">Tame Impala</text>

  <rect x="50" y="102" width="3" height="7" rx="1.5" fill="#1DB954" opacity="0.4"/>
  <rect x="57" y="98" width="3" height="13" rx="1.5" fill="#1DB954" opacity="0.8"/>
  <rect x="64" y="102" width="3" height="9" rx="1.5" fill="#1DB954" opacity="0.35"/>
  <rect x="71" y="96" width="3" height="16" rx="1.5" fill="#1DB954" opacity="0.9"/>
  <rect x="78" y="100" width="3" height="11" rx="1.5" fill="#1DB954" opacity="0.5"/>
  <rect x="85" y="103" width="3" height="6" rx="1.5" fill="#1DB954" opacity="0.3"/>
  <rect x="92" y="97" width="3" height="14" rx="1.5" fill="#1DB954" opacity="0.7"/>
  <rect x="99" y="101" width="3" height="9" rx="1.5" fill="#1DB954" opacity="0.45"/>
  <rect x="106" y="95" width="3" height="17" rx="1.5" fill="#1DB954" opacity="0.85"/>
  <rect x="113" y="99" width="3" height="11" rx="1.5" fill="#1DB954" opacity="0.55"/>

  <image href="data:image/jpeg;base64,{b64}" x="75" y="145" width="250" height="250" clip-path="url(#cc)"/>

  <a href="https://open.spotify.com/track/7uLz3wJ1fVwL7JfScdMX6R" target="_blank">
    <rect x="0" y="0" width="400" height="420" fill="transparent"/>
  </a>
</svg>'''

with open('dist/spotify.svg', 'w', encoding='utf-8') as f:
    f.write(svg)
print(f'SVG: {len(svg)} chars, Base64: {len(b64)}')
