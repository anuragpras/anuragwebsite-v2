import os
import re

analytics_code = """
<script type="module">
  import { initializeApp } from "https://www.gstatic.com/firebasejs/12.15.0/firebase-app.js";
  import { getAnalytics } from "https://www.gstatic.com/firebasejs/12.15.0/firebase-analytics.js";

  const firebaseConfig = {
    apiKey: "AIzaSyBRvCXwMgg-bti7NCeFXqUiO3KWklsgW8c",
    authDomain: "anu-raag.firebaseapp.com",
    projectId: "anu-raag",
    storageBucket: "anu-raag.firebasestorage.app",
    messagingSenderId: "235852262265",
    appId: "1:235852262265:web:d9924dccc453cca2451da8",
    measurementId: "G-B5Y6T3SZL9"
  };

  const app = initializeApp(firebaseConfig);
  const analytics = getAnalytics(app);
</script>
</body>"""

for root, dirs, files in os.walk('.'):
    if '.git' in root or '.vercel' in root or 'node_modules' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                html = f.read()
            
            # Prevent double insertion
            if 'G-B5Y6T3SZL9' not in html:
                html = html.replace('</body>', analytics_code)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(html)
                print(f"Added Analytics to {filepath}")
