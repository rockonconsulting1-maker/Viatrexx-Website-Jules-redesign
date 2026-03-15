#!/usr/bin/env python3
import sys
import json

def generate_redirects(snapshot_path):
    try:
        with open(snapshot_path, 'r') as f:
            data = json.load(f)

        pages = data.get("pages", [])
        if not pages:
             pages = [k for k in data.keys() if k != "pages"]

        redirects = []
        for page in pages:
            old_path = page.strip()
            if old_path.startswith('./'):
                old_path = old_path[1:] # Keep leading slash for redirect
            elif not old_path.startswith('/'):
                old_path = '/' + old_path

            # Skip assets and errors
            if "/wp-content/" in old_path or "fonts.gstatic.com" in old_path or "cdn-cgi" in old_path:
                continue

            new_path = old_path

            # Flattening logic
            if "/product-details/product/" in old_path:
                new_path = old_path.replace("/product-details/product/", "/products/")
            elif "/products/collections/" in old_path:
                new_path = old_path.replace("/products/collections/", "/collections/")
            elif old_path == "/products.html":
                new_path = "/products"
            elif old_path == "/home.html" or old_path == "/index.html":
                new_path = "/"

            # Clean up extensions
            if new_path.endswith(".html"):
                new_path = new_path[:-5]

            # Standardize index pages
            if new_path.endswith("/index"):
                new_path = new_path[:-6]

            if not new_path:
                new_path = "/"

            if old_path != new_path:
                redirects.append({
                    "from": old_path,
                    "to": new_path,
                    "type": 301
                })

        return sorted(redirects, key=lambda x: x['from'])
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    snapshot_file = "gathering/site_snapshot.json"
    if len(sys.argv) > 1:
        snapshot_file = sys.argv[1]

    result = generate_redirects(snapshot_file)
    print(json.dumps(result, indent=2))
