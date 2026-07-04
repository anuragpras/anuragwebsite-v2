import os
import re

pages = []
for root, dirs, files in os.walk('.'):
    if '.git' in root or '.vercel' in root:
        continue
    for f in files:
        if f == 'index.html':
            pages.append(os.path.join(root, f))

print('=== FONT AUDIT ===')
for p in sorted(pages):
    with open(p, encoding='utf-8') as f:
        html = f.read()
    gfont = 'Plus+Jakarta+Sans' in html
    inline_fonts = re.findall(r'font-family\s*:\s*([^;"\n]+)', html)
    inline_fonts = [x.strip() for x in inline_fonts if 'Plus' not in x and 'inherit' not in x and 'var(' not in x]
    print(p)
    print('  GFont loaded:', gfont)
    if inline_fonts:
        print('  NON-STANDARD font-family overrides:', inline_fonts[:5])

print()
print('=== CSS GLOBAL ===')
with open('css/style.css', encoding='utf-8') as f:
    css = f.read()

# Check for any hardcoded font families
css_fonts = re.findall(r'font-family\s*:\s*([^;{]+)', css)
for cf in css_fonts:
    print(' CSS font-family:', cf.strip()[:80])
