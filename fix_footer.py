import os
import glob
import re

css_path = 'css/style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Replace the footer block
new_footer_css = """footer {
  text-align: center;
  font-size: 0.8rem;
  color: var(--text-muted);
}
footer .wrap {
  border-top: 1px solid var(--border);
  padding: 1rem 0;
  max-width: var(--max-w);
  margin: 0 auto;
}"""

css = re.sub(r'footer\s*\{[^}]*\}', new_footer_css, css)

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

# Now break CSS cache in all HTML files
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
    
    # Replace style.css with style.css?v=3
    html = re.sub(r'href="/css/style\.css(\?v=\d+)?"', 'href="/css/style.css?v=3"', html)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

print("Updated footer width and broke CSS cache.")
