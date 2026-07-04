import re

# 1. Update gallery/index.html
with open('gallery/index.html', 'r', encoding='utf-8') as f:
    html = f.read()
# Remove <h1>Gallery</h1>
html = re.sub(r'<h1>Gallery</h1>\s*', '', html)
with open('gallery/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Update blog/index.html
with open('blog/index.html', 'r', encoding='utf-8') as f:
    html = f.read()
# Remove <h1>Blog</h1>
html = re.sub(r'<h1>Blog</h1>\s*', '', html)
# We also want to style the post list with borders to match screenshot
html = html.replace('<div class="post-list">', '<div class="post-list" style="border-top: 1px solid var(--border); border-bottom: 1px solid var(--border); margin-top: 1rem; padding-top: 1rem; padding-bottom: 1rem;">')
with open('blog/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 3. Update projects/index.html
with open('projects/index.html', 'r', encoding='utf-8') as f:
    html = f.read()
# Remove <h1>Projects</h1>
html = re.sub(r'<h1>Projects</h1>\s*', '', html)
with open('projects/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
    
# 4. Update blog/first-post/index.html just in case (remove "<- Blog" if present)
with open('blog/first-post/index.html', 'r', encoding='utf-8') as f:
    html = f.read()
html = re.sub(r'<a class="back" href="/blog/">← Blog</a>\s*', '', html)
with open('blog/first-post/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Removed redundant H1 tags.")
