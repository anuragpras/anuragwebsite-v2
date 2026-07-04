import re

# 1. Update css/style.css
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = css.replace('.r-org a { border-bottom: 1px solid transparent;', '.r-org a { border-bottom: 1px solid var(--border);')

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# 2. Update resume/index.html
with open('resume/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('<span class="r-org">Rukhmani Devi Public School, Bhopal</span>', '<span class="r-org"><a href="https://www.rukhmanidevischool.com/" target="_blank" rel="noopener">Rukhmani Devi Public School, Bhopal</a></span>')

html = html.replace('<span class="r-org">Holy Family Convent Sr. Sec. School, Bhopal</span>', '<span class="r-org"><a href="https://hfcsbhopal.edu.in/" target="_blank" rel="noopener">Holy Family Convent Sr. Sec. School, Bhopal</a></span>')

# Just in case VIT wasn't updated properly or if they want to ensure it has the same format
html = html.replace('<span class="r-org">Vellore Institute of Technology, Bhopal</span>', '<span class="r-org"><a href="https://vitbhopal.ac.in/" target="_blank" rel="noopener">Vellore Institute of Technology, Bhopal</a></span>')

with open('resume/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated links and CSS.")
