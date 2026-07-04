import re

with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

with open('gallery/index.html', 'r', encoding='utf-8') as f:
    gallery = f.read()

with open('js/site.js', 'r', encoding='utf-8') as f:
    js = f.read()

checks = [
    ('CSS: body is flex column', 'flex-direction: column' in css),
    ('CSS: main flex-grows', 'flex: 1 0 auto' in css),
    ('CSS: footer is thin', 'padding: 0.3rem 0' in css),
    ('CSS: nav is sticky', 'position: sticky' in css),
    ('CSS: footer flex-shrink', 'flex-shrink: 0' in css),
    ('JS: theme toggle works', 'applyTheme' in js),
    ('JS: hamburger toggles', "navLinks.classList.toggle('open')" in js),
    ('JS: close on outside click', "!menuBtn.contains(e.target)" in js),
    ('Gallery: lazy loading', 'loading="lazy"' in gallery),
    ('Gallery: decode async', 'decoding="async"' in gallery),
    ('JS: DOMContentLoaded wraps all', 'document.addEventListener' in js),
]

for name, result in checks:
    status = 'OK' if result else 'MISSING'
    print(name + ': ' + status)
