import os
from bs4 import BeautifulSoup

def improve_a11y(filepath):
    print(f"Improving a11y for {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    soup = BeautifulSoup(content, 'html.parser')

    # 1. Inject focus ring style
    # We'll put it in the first <head> we find
    style_content = """
    /* High-visibility focus ring injected by Experience Agent */
    *:focus {
        outline: 3px solid #3B82F6 !important;
        outline-offset: 2px !important;
    }
    """
    style_tag = soup.new_tag('style', type="text/css")
    style_tag.string = style_content

    head = soup.find('head')
    if head:
        head.append(style_tag)
    else:
        # Fallback to appending to the beginning of the soup
        soup.insert(0, style_tag)

    # 2. Check aria-labels on buttons
    for btn in soup.find_all('button'):
        if not btn.get('aria-label') and not btn.get_text(strip=True):
            cls = btn.get('class', [])
            if any('hamburger' in c or 'mobile-menu' in c for c in cls):
                btn['aria-label'] = 'Open mobile menu'
                print(f"Added aria-label to hamburger menu in {filepath}")
            elif any('close' in c for c in cls):
                btn['aria-label'] = 'Close'
                print(f"Added aria-label to close button in {filepath}")

    # 3. Check social links in footer
    # Usually social links have an icon and a title or title attribute
    for a in soup.find_all('a'):
        title = a.get('title')
        if title and not a.get('aria-label'):
            a['aria-label'] = title
            print(f"Added aria-label '{title}' to link in {filepath}")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(soup.prettify())

if __name__ == "__main__":
    for page in ['index.html', 'home.html']:
        improve_a11y(page)
