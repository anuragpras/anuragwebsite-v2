import os
import re

html_files = []
for root, dirs, files in os.walk('.'):
    if 'node_modules' in root or '.git' in root or '.vercel' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            html_files.append(os.path.join(root, file))

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    html = re.sub(r'href="/css/style\.css\?v=\d+"', 'href="/css/style.css?v=8"', html)
    html = re.sub(r'src="/js/site\.js(\?v=\d+)?"', 'src="/js/site.js?v=8"', html)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

print('Updated all cache busters to v=8')
