import requests, re

url = 'https://github-readme-streak-stats.herokuapp.com?user=ichramal&theme=midnight-purple&hide_border=true&background=0d1117'
r = requests.get(url, timeout=15)
body = r.content.decode()
rects = re.findall(r'<rect[^>]*>', body)
for rect in rects[:5]:
    print(rect)
bgs = re.findall(r'fill=[\'"]#?[0-9a-fA-F]+[\'"]', body)
for b in bgs[:10]:
    print(b)
