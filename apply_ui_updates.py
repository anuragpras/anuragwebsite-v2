import os
import re

# 1. Update index.html (Favicon instead of hand)
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('<img src="/img/waving_hand_animated_default.png" width="32" height="32" alt="Wave"', '<img src="/icons8-circle-96.png" width="26" height="26" alt="Logo"')
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)


# 2. Update style.css (Gallery grid & Projects fluidity)
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace gallery masonry with standard grid
old_gallery = """.gallery-grid {
  column-count: 1;
  column-gap: 1rem;
}
@media (min-width: 600px) { .gallery-grid { column-count: 2; } }
@media (min-width: 900px) { .gallery-grid { column-count: 3; } }
.g-item {
  margin-bottom: 1rem;
  break-inside: avoid;
  cursor: pointer;
  border-radius: var(--r);
  overflow: hidden;
}"""

new_gallery = """.gallery-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
  gap: 1rem;
}
.g-item {
  aspect-ratio: 1 / 1;
  cursor: pointer;
  border-radius: var(--r);
  overflow: hidden;
  background-color: var(--border);
}
.g-item img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}"""
if '.gallery-grid {' in css:
    # Use regex to replace the gallery grid part
    css = re.sub(r'\.gallery-grid\s*{[^}]+}\s*@media[^}]+\s*}\s*}\s*@media[^}]+\s*}\s*}\s*\.g-item\s*{[^}]+}', new_gallery, css, flags=re.DOTALL)
    # Just in case regex fails, I'll forcefully inject it if not replaced properly, but I'll write a safer regex
    css = re.sub(r'\.gallery-grid\s*{.*?\.g-item\s*{.*?}', new_gallery, css, flags=re.DOTALL|re.IGNORECASE)
    
# Let's ensure new_gallery is in there, if not append it. 
# Also add fluid fade-in for images
fluid_css = """
/* Fluid image loading */
img {
  animation: fadeIn 0.4s ease-out forwards;
}
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}
"""
css += fluid_css

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)


# 3. Contact Page Update
contact_html = """<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Contact — Anurag Prasad</title>
  <meta name="description" content="Get in touch with Anurag Prasad — email and location.">
  <link rel="icon" href="/icons8-circle-96.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/css/style.css">
  <script>(function(){var t=localStorage.getItem('ap-theme')||(window.matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light');document.documentElement.setAttribute('data-theme',t);})();</script>
  <style>
    .contact-subtitle {
      color: var(--text-muted);
      margin-top: 0.5rem;
      margin-bottom: 2rem;
    }
    .c-block {
      background: var(--bg-alt);
      padding: 1.5rem;
      border-radius: var(--r);
      border: 1px solid var(--border);
    }
    .contact-form {
      margin-top: 2rem;
      background: var(--bg-alt);
      padding: 2rem;
      border-radius: var(--r);
      border: 1px solid var(--border);
    }
    .contact-form h2 {
      margin-top: 0;
      margin-bottom: 1.5rem;
      font-size: 1.25rem;
    }
    .form-row {
      display: flex;
      flex-direction: column;
      gap: 1rem;
      margin-bottom: 1rem;
    }
    @media (min-width: 600px) {
      .form-row { flex-direction: row; }
      .form-row .form-group { flex: 1; }
    }
    .form-group {
      display: flex;
      flex-direction: column;
      margin-bottom: 1rem;
    }
    .form-group label {
      font-size: 0.8rem;
      font-weight: 700;
      text-transform: uppercase;
      margin-bottom: 0.5rem;
      color: var(--text-muted);
    }
    .form-group input, .form-group textarea {
      padding: 0.8rem;
      border: 1px solid var(--border);
      background: var(--bg);
      color: var(--text);
      border-radius: 6px;
      font-family: inherit;
    }
    .form-group input:focus, .form-group textarea:focus {
      outline: 2px solid var(--accent);
      border-color: transparent;
    }
    .form-group textarea {
      resize: vertical;
      min-height: 120px;
    }
    .send-btn {
      background: var(--accent);
      color: #fff;
      border: none;
      padding: 0.8rem 1.5rem;
      border-radius: 6px;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
    }
    .send-btn:hover {
      opacity: 0.9;
    }
  </style>
</head>
<body>

<nav>
  <div class="nav-inner">
    <a class="nav-logo" href="/">Anurag Prasad</a>
    <div class="nav-right">
      <ul class="nav-links">
        <li><a href="/">About</a></li>
        <li><a href="/projects/">Projects</a></li>
        <li><a href="/gallery/">Gallery</a></li>
        <li><a href="/blog/">Blog</a></li>
        <li><a href="/contact/">Contact</a></li>
        <li><a href="/resume/">Resume</a></li>
      </ul>
      <button id="theme-btn" aria-label="Toggle theme">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>
      </button>
      <button id="menu-btn" aria-label="Open menu" aria-expanded="false">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
      </button>
    </div>
  </div>
</nav>

<main>
  <div class="wrap">

    <div class="page-head" style="margin-bottom: 0;">
      <h1>Get in Touch</h1>
      <p class="contact-subtitle">Feel free to reach out for collaboration, projects, or just a quick chat.</p>
    </div>

    <div class="contact-cols">
      <div class="c-block">
        <h3 style="display:flex; align-items:center; gap:0.5rem;"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="color:var(--accent);"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg> EMAIL</h3>
        <p>
          <a href="mailto:ianuragprasad@gmail.com">ianuragprasad@gmail.com</a><br>
          <a href="mailto:meanuragprasad@gmail.com">meanuragprasad@gmail.com</a>
        </p>
      </div>
      <div class="c-block">
        <h3 style="display:flex; align-items:center; gap:0.5rem;"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="color:var(--accent);"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg> LOCATION</h3>
        <p>Bhopal, Madhya Pradesh, India</p>
      </div>
    </div>

    <div class="contact-form">
      <h2>Send a Message</h2>
      <form action="#" method="POST">
        <div class="form-row">
          <div class="form-group">
            <label for="name">Name *</label>
            <input type="text" id="name" name="name" required>
          </div>
          <div class="form-group">
            <label for="email">Email *</label>
            <input type="email" id="email" name="email" required>
          </div>
        </div>
        <div class="form-group">
          <label for="subject">Subject</label>
          <input type="text" id="subject" name="subject">
        </div>
        <div class="form-group">
          <label for="message">Message *</label>
          <textarea id="message" name="message" required></textarea>
        </div>
        <button type="submit" class="send-btn">
          Send Message 
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>
        </button>
      </form>
    </div>

  </div>
</main>

<footer>
  <div class="wrap">अनुराग प्रसाद</div>
</footer>

<script src="/js/site.js"></script>
</body>
</html>"""

with open('contact/index.html', 'w', encoding='utf-8') as f:
    f.write(contact_html)

