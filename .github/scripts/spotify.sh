#!/bin/bash
set -e

mkdir -p dist

TOKEN=$(curl -s -X POST "https://accounts.spotify.com/api/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=refresh_token&refresh_token=${SPOTIFY_REFRESH_TOKEN}" \
  --user "${SPOTIFY_CLIENT_ID}:${SPOTIFY_CLIENT_SECRET}" | jq -r '.access_token')

# Try currently playing first
curl -s -X GET "https://api.spotify.com/v1/me/player/currently-playing" \
  -H "Authorization: Bearer $TOKEN" > current.json

if jq -e '.is_playing == true' current.json > /dev/null 2>&1; then
  ARTIST=$(jq -r '.item.artists[0].name' current.json)
  TRACK=$(jq -r '.item.name' current.json)
  IMG=$(jq -r '.item.album.images[0].url' current.json)
  echo "Now playing: $TRACK - $ARTIST"
else
  # Fallback to recently played
  curl -s -X GET "https://api.spotify.com/v1/me/player/recently-played?limit=1" \
    -H "Authorization: Bearer $TOKEN" > recent.json
  ARTIST=$(jq -r '.items[0].track.artists[0].name' recent.json 2>/dev/null)
  TRACK=$(jq -r '.items[0].track.name' recent.json 2>/dev/null)
  IMG=$(jq -r '.items[0].track.album.images[0].url' recent.json 2>/dev/null)
  
  if [ "$TRACK" = "null" ] || [ -z "$TRACK" ]; then
    echo "No tracks found, showing placeholder"
    cat > dist/spotify.svg << 'SVGEOF'
<svg xmlns="http://www.w3.org/2000/svg" width="400" height="90" viewBox="0 0 400 90">
  <rect width="400" height="90" rx="14" fill="#1a1a2e"/>
  <rect x="15" y="15" width="60" height="60" rx="8" fill="#2a2a4e"/>
  <text x="90" y="38" font-family="system-ui,sans-serif" font-size="12" fill="#6a0dad" font-weight="bold" letter-spacing="2">SPOTIFY</text>
  <text x="90" y="55" font-family="system-ui,sans-serif" font-size="14" fill="#8b949e">No Data</text>
  <text x="90" y="70" font-family="system-ui,sans-serif" font-size="11" fill="#484f58">Connect Spotify to see tracks</text>
  <circle cx="350" cy="45" r="15" fill="#1DB954"/>
  <polygon points="346,38 346,52 356,45" fill="#000"/>
</svg>
SVGEOF
    exit 0
  fi
  echo "Last played: $TRACK - $ARTIST"
fi

cat > dist/spotify.svg << SVGEOF
<svg xmlns="http://www.w3.org/2000/svg" width="400" height="100" viewBox="0 0 400 100">
  <defs><clipPath id="c"><rect width="60" height="60" rx="8"/></clipPath></defs>
  <rect width="400" height="100" rx="14" fill="#1a1a2e"/>
  <image href="$IMG" x="15" y="20" width="60" height="60" clip-path="url(#c)"/>
  <text x="90" y="40" font-family="system-ui,sans-serif" font-size="12" fill="#6a0dad" font-weight="bold" letter-spacing="2">SPOTIFY</text>
  <text x="90" y="58" font-family="system-ui,sans-serif" font-size="14" fill="#ffffff" font-weight="bold">$TRACK</text>
  <text x="90" y="74" font-family="system-ui,sans-serif" font-size="12" fill="#8b949e">$ARTIST</text>
  <circle cx="350" cy="50" r="15" fill="#1DB954"/>
  <polygon points="346,43 346,57 358,50" fill="#000"/>
</svg>
SVGEOF
