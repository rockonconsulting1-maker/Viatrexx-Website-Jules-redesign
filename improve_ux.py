import os
from bs4 import BeautifulSoup

def apply_ux_fixes(filepath):
    print(f"Applying UX fixes for {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    soup = BeautifulSoup(content, 'html.parser')

    # 1. Update header z-index to 1000
    header = soup.find('header')
    if header:
        classes = header.get('class', [])
        if 'z-50' in classes:
            classes.remove('z-50')
        if 'z-1000' not in classes:
            classes.append('z-1000')
        header['class'] = classes

        # Also need to make sure z-1000 is defined in CSS or use inline style
        # Tailwind doesn't have z-1000 by default usually, so let's use inline style
        header['style'] = header.get('style', '') + '; z-index: 1000;'
        print(f"Set z-index: 1000 on header in {filepath}")

    # 2. Ensure top-banner is relative
    banner = soup.find(id='top-banner')
    if banner:
        banner['style'] = banner.get('style', '') + '; position: relative;'
        print(f"Ensured top-banner is relative in {filepath}")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(soup.prettify())

if __name__ == "__main__":
    for page in ['index.html', 'home.html']:
        apply_ux_fixes(page)
