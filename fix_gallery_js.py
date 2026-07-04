import os
import re

css_path = 'css/style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Fix the duplicate .g-item img that overrides height to auto
# Remove the second block completely
css = css.replace('.g-item img {\n  width: 100%;\n  height: auto;\n  display: block;\n  transition: transform 0.28s ease;\n}', '')

# Add the transition to the first block
css = css.replace('.g-item img {\n  width: 100%;\n  height: 100%;\n  object-fit: cover;\n  display: block;\n}', '.g-item img {\n  width: 100%;\n  height: 100%;\n  object-fit: cover;\n  display: block;\n  transition: transform 0.28s ease;\n}')

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)


js_path = 'js/site.js'
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

mobile_menu_fix = """  // ---------- Mobile menu ----------
  const menuBtn = document.getElementById('menu-btn');
  const navLinks = document.querySelector('.nav-links');
  if (menuBtn && navLinks) {
    menuBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      navLinks.classList.toggle('open');
      const open = navLinks.classList.contains('open');
      menuBtn.setAttribute('aria-expanded', open);
    });
    // Close on link click
    navLinks.querySelectorAll('a').forEach(a => {
      a.addEventListener('click', () => navLinks.classList.remove('open'));
    });
    // Close on click outside
    document.addEventListener('click', (e) => {
      if (navLinks.classList.contains('open') && !navLinks.contains(e.target) && e.target !== menuBtn) {
        navLinks.classList.remove('open');
        menuBtn.setAttribute('aria-expanded', false);
      }
    });
  }"""

js = re.sub(r'  // ---------- Mobile menu ----------\n.*?(?=\n\n|\Z)', mobile_menu_fix, js, flags=re.DOTALL)

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js)

print("Fixed CSS and JS")
