import requests
from io import BytesIO
from PIL import Image
import base64

r = requests.get('https://i.scdn.co/image/ab67616d0000b2739e1cfc756886ac782e363d79')
img = Image.open(BytesIO(r.content))

img80 = img.resize((80, 80), Image.LANCZOS)
buf80 = BytesIO()
img80.save(buf80, 'JPEG', quality=85)
b64_80 = base64.b64encode(buf80.getvalue()).decode()

# ============================================================
# NOVATORM STYLE (320x100) - pure SVG, transparent bg
# ============================================================
novatorem = f'''<svg width="320" height="100" viewBox="0 0 320 100" xmlns="http://www.w3.org/2000/svg" aria-labelledby="cardTitle" role="img">
  <title id="cardTitle">Now playing on Spotify</title>
  <defs>
    <clipPath id="mc"><rect x="10" y="10" width="80" height="80" rx="3"/></clipPath>
  </defs>
  <image href="data:image/jpeg;base64,{b64_80}" x="10" y="10" width="80" height="80" clip-path="url(#mc)"/>
  <circle cx="104" cy="18" r="6" fill="#53b14f"/>
  <polygon points="102,14 102,22 108,18" fill="#fff"/>
  <text x="114" y="22" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,sans-serif" font-size="11" font-weight="bold" fill="#53b14f">NOW PLAYING</text>
  <rect x="204" y="11" width="2" height="6" rx="1" fill="#006eff" opacity="0.35"/>
  <rect x="208" y="8" width="2" height="12" rx="1" fill="#006eff" opacity="1"/>
  <rect x="212" y="13" width="2" height="4" rx="1" fill="#006eff" opacity="0.3"/>
  <rect x="216" y="9" width="2" height="10" rx="1" fill="#006eff" opacity="0.7"/>
  <rect x="220" y="11" width="2" height="6" rx="1" fill="#006eff" opacity="0.5"/>
  <text x="104" y="48" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,sans-serif" font-size="16" font-weight="500" fill="#555">Tame Impala</text>
  <text x="104" y="68" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,sans-serif" font-size="15" fill="#999">Let It Happen</text>
  <a href="https://open.spotify.com/track/7uLz3wJ1fVwL7JfScdMX6R" target="_blank">
    <rect x="0" y="0" width="320" height="100" fill="transparent"/>
  </a>
</svg>'''

with open('dist/spotify-novatorem.svg', 'w', encoding='utf-8') as f:
    f.write(novatorem)
print(f'novatorem: {len(novatorem)} chars')

# ============================================================
# COMPACT STYLE (320x400) - pure SVG, dark bg
# ============================================================
img300 = img.resize((300, 300), Image.LANCZOS)
buf300 = BytesIO()
img300.save(buf300, 'JPEG', quality=85)
b64_300 = base64.b64encode(buf300.getvalue()).decode()

compact = f'''<svg width="320" height="400" viewBox="0 0 320 400" xmlns="http://www.w3.org/2000/svg" aria-labelledby="cardTitle" role="img">
  <title id="cardTitle">Now playing on Spotify</title>
  <defs>
    <clipPath id="mc2"><rect x="10" y="36" width="300" height="300" rx="8"/></clipPath>
  </defs>
  <rect width="320" height="400" rx="12" fill="#121212"/>
  <circle cx="108" cy="14" r="5" fill="#1DB954"/>
  <polygon points="106.5,11 106.5,17 111,14" fill="#fff"/>
  <text x="118" y="18" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,sans-serif" font-size="12" font-weight="bold" fill="#1DB954" letter-spacing="1">NOW PLAYING</text>
  <circle cx="218" cy="14" r="5" fill="#1DB954"/>
  <polygon points="216.5,11 216.5,17 221,14" fill="#fff"/>
  <image href="data:image/jpeg;base64,{b64_300}" x="10" y="36" width="300" height="300" clip-path="url(#mc2)"/>
  <text x="160" y="360" text-anchor="middle" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,sans-serif" font-size="20" font-weight="bold" fill="#fff">Tame Impala</text>
  <text x="160" y="382" text-anchor="middle" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,sans-serif" font-size="16" fill="#b3b3b3">Let It Happen</text>
  <a href="https://open.spotify.com/track/7uLz3wJ1fVwL7JfScdMX6R" target="_blank">
    <rect x="0" y="0" width="320" height="400" fill="transparent"/>
  </a>
</svg>'''

with open('dist/spotify-compact.svg', 'w', encoding='utf-8') as f:
    f.write(compact)
print(f'compact: {len(compact)} chars')
