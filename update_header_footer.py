import os
import glob
import re

html_files = [
    'index.html',
    'projects/index.html',
    'gallery/index.html',
    'blog/index.html',
    'blog/first-post/index.html',
    'contact/index.html',
    'resume/index.html'
]

# The new Nav Logo
nav_logo_old = '<a class="nav-logo" href="/">Anurag Prasad</a>'
nav_logo_new = '<a class="nav-logo" href="/" style="display:flex; align-items:center; gap:0.5rem;"><img src="/icons8-circle-96.png" width="18" height="18" alt="Logo" style="opacity: 0.8; margin-top: 1px;"> Anurag Prasad <span style="font-weight:400; opacity:0.8;">| अनुराग प्रसाद</span></a>'

# The new Footer
footer_old_pattern = r'<footer>\s*<div class="wrap">अनुराग प्रसाद</div>\s*</footer>'
footer_new = '<footer>\n  <div class="wrap">© 2026 Anurag Prasad · अनुराग प्रसाद</div>\n</footer>'

for file in html_files:
    if not os.path.exists(file):
        continue
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update Nav Logo
    content = content.replace(nav_logo_old, nav_logo_new)

    # Update Footer
    content = re.sub(footer_old_pattern, footer_new, content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

# Revert the h1 on the index page
with open('index.html', 'r', encoding='utf-8') as f:
    idx = f.read()

idx = re.sub(r'<h1 class="about-name".*?</h1>', '<h1 class="about-name">Anurag Prasad</h1>', idx)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(idx)

# Update gallery text
with open('gallery/index.html', 'r', encoding='utf-8') as f:
    gal = f.read()
gal = gal.replace('<p>Stills by Anurag</p>', '<p>⛺ stills by अनुराग</p>')
with open('gallery/index.html', 'w', encoding='utf-8') as f:
    f.write(gal)

print("Updates applied to all pages.")
