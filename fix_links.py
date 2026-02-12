import re

replacements = {
    '673e414c8be63738e401ec8d': '/assets/optimized/hexagon-bg.webp',
    '673e4811a46b3069cc83e4a9': '/assets/optimized/practitioner-guide.webp',
    '673e4812a46b3017a483e4aa': '/assets/optimized/ez-heartbeat-science.webp',
    '673e4812f86a9f0f9c211cc5': '/assets/optimized/clinical-research.webp',
    '68055d66768a58fa6673261c': '/assets/optimized/card-image.webp',
}

def fix_file(filename):
    with open(filename, 'r') as f:
        content = f.read()

    for key, val in replacements.items():
        # Match anything that looks like a URL or path containing the key
        # and replace the whole thing with the new path
        pattern = r'[^"\' ]*' + re.escape(key) + r'[^"\' ]*'
        content = re.sub(pattern, val, content)

    with open(filename, 'w') as f:
        f.write(content)

fix_file('index.html')
fix_file('home.html')
