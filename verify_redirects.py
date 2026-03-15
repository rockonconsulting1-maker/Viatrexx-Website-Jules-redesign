import re

redirect_rules = [
    (r'^/index\.html$', '/'),
    (r'^/home\.html$', '/'),
    (r'^/about\.html$', '/about'),
    (r'^/products\.html$', '/products'),
    (r'^/products/collections/index\.html$', '/collections'),
    (r'^/product-details/product/(.+)\.html$', '/products/\1'),
    (r'^/products/collections/(.+)\.html$', '/collections/\1'),
]

test_cases = [
    ('/index.html', '/'),
    ('/home.html', '/'),
    ('/about.html', '/about'),
    ('/products.html', '/products'),
    ('/product-details/product/aap-im-1.html', '/products/aap-im-1'),
    ('/products/collections/detox-drainage.html', '/collections/detox-drainage'),
    ('/products/collections/index.html', '/collections'),
]

def verify():
    all_passed = True
    for source, expected in test_cases:
        matched = False
        for pattern, dest_template in redirect_rules:
            match = re.match(pattern, source)
            if match:
                actual = dest_template
                if "\1" in dest_template and match.groups():
                    actual = dest_template.replace("\1", match.group(1))

                if actual == expected:
                    print(f"PASS: {source} -> {actual}")
                    matched = True
                    break
                else:
                    # Continue searching if it matched a too-broad pattern incorrectly
                    # But in this list, the first match should be the correct one if ordered properly
                    print(f"DEBUG: matched {pattern} but got {actual} (expected {expected})")
                    continue
        if not matched:
            print(f"FAIL: {source} did not match any correct redirect rule")
            all_passed = False
    return all_passed

if __name__ == "__main__":
    if verify():
        print("\nAll redirect verifications PASSED.")
    else:
        print("\nRedirect verifications FAILED.")
        exit(1)
