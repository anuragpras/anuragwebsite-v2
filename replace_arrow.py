import re

with open('projects/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

svg_icon = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="opacity:0.4; margin-left:4px; vertical-align:middle; position:relative; top:-2px;"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>'

html = html.replace(' ↗</a>', f'{svg_icon}</a>')

with open('projects/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Replaced unicode arrow with SVG icon in projects.")
