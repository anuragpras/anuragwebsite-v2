import re

with open('gallery/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

def add_lazy(match):
    tag = match.group(0)
    if 'loading=' not in tag:
        tag = tag.replace('<img ', '<img loading="lazy" decoding="async" ')
    return tag

html = re.sub(r'<img\s+src="/gallery/images/[^"]*"[^>]*>', add_lazy, html)

with open('gallery/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Added lazy loading to gallery images')
