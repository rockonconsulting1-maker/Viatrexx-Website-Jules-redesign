import os
from bs4 import BeautifulSoup

def fix_html_file(filepath, is_home=False):
    print(f"Processing {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    soup = BeautifulSoup(content, 'html.parser')

    # 1. Replace href="#" with javascript:void(0) in dropdowns
    for a in soup.find_all('a', href='#'):
        a['href'] = 'javascript:void(0)'

    # 2. Add aria-current="page" to active link
    nav_links = soup.find_all('a', class_='nav-link')
    for link in nav_links:
        if is_home and link.get_text(strip=True).lower() == 'home':
            link['aria-current'] = 'page'
            print(f"Added aria-current='page' to {link.get_text(strip=True)}")

    # 3. Ensure external links have rel="noopener noreferrer"
    for a in soup.find_all('a', href=True):
        href = a['href']
        if href.startswith('http') and 'viatrexx.com' not in href and 'viatrexx.ca' not in href:
            if a.get('target') == '_blank':
                a['rel'] = 'noopener noreferrer'

    # 4. Correct asset paths with incorrect ../ prefixes
    tags_attrs = {
        'link': 'href',
        'script': 'src',
        'img': 'src',
        'a': 'href'
    }

    for tag, attr in tags_attrs.items():
        for el in soup.find_all(tag, **{attr: True}):
            val = el[attr]
            if val.startswith('../'):
                # For files in root, ../ is always wrong
                new_val = val[3:]
                el[attr] = new_val

    # 5. Fix multiple body tags or nested html (common in this mirror)
    # BeautifulSoup's str(soup) might help clean this up, but the structure is very broken.
    # Actually, I'll just write it back for now and see the result.

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(soup.prettify())

if __name__ == "__main__":
    fix_html_file('index.html', is_home=True)
    fix_html_file('home.html', is_home=True)
    print("Fixed index.html and home.html")
