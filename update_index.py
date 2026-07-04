import re

# 1. Update style.css
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()
# Remove transitions causing lag
css = re.sub(r'transition:\s*background\s*var\(--t\),\s*color\s*var\(--t\);', '', css)
css = re.sub(r'transition:\s*transform\s*0.28s\s*ease,\s*opacity\s*0.28s\s*ease;', 'transition: transform 0.28s ease;', css)
css = css.replace('opacity: 0.88;', '') # remove hover opacity

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# 2. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add Hindi text and emoji beside name
html = html.replace('<h1 class="about-name">Anurag Prasad</h1>', '<h1 class="about-name" style="display:flex; align-items:center; gap:0.5rem; flex-wrap:wrap;">Anurag Prasad <img src="/img/waving_hand_animated_default.png" width="32" height="32" alt="Wave" style="vertical-align:middle; position:relative; top:-2px;"> <span style="font-size:0.55em; color:var(--text-muted); font-weight:500; margin-top:2px;">अनुराग प्रसाद</span></h1>')

# Remove duplicate buttons
html = re.sub(r'<div class="about-buttons">.*?</div>', '', html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
