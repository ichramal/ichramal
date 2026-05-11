#!/bin/bash

mkdir -p dist

TOKEN=$(curl -s -X POST "https://accounts.spotify.com/api/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=refresh_token&refresh_token=${SPOTIFY_REFRESH_TOKEN}" \
  --user "${SPOTIFY_CLIENT_ID}:${SPOTIFY_CLIENT_SECRET}" | jq -r '.access_token')

if [ -z "$TOKEN" ] || [ "$TOKEN" = "null" ]; then
  echo "No token, using default track"
  IMG="https://i.scdn.co/image/ab67616d0000b273c0bd2281ef27489f00953b22"
  TRACK="Let It Happen"
  ARTIST="Tame Impala"
else
  curl -s -X GET "https://api.spotify.com/v1/me/player/currently-playing" \
    -H "Authorization: Bearer $TOKEN" > current.json

  if jq -e '.is_playing == true' current.json > /dev/null 2>&1; then
    ARTIST=$(jq -r '.item.artists[0].name' current.json 2>/dev/null)
    TRACK=$(jq -r '.item.name' current.json 2>/dev/null)
    IMG=$(jq -r '.item.album.images[0].url' current.json 2>/dev/null)
  else
    echo "Not playing, using default"
    IMG="https://i.scdn.co/image/ab67616d0000b273c0bd2281ef27489f00953b22"
    TRACK="Let It Happen"
    ARTIST="Tame Impala"
  fi
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
echo "Done: $TRACK - $ARTIST"
