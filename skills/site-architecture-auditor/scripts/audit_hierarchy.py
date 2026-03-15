#!/usr/bin/env python3
import sys
import json
import os

def build_tree(pages):
    tree = {}
    for page in pages:
        # Clean the path
        path = page.strip()
        if path.startswith('./'):
            path = path[2:]

        parts = path.split('/')
        current = tree
        for part in parts:
            if part not in current:
                current[part] = {}
            current = current[part]
    return tree

def get_current_hierarchy(snapshot_path):
    try:
        with open(snapshot_path, 'r') as f:
            data = json.load(f)

        pages = data.get("pages", [])
        if not pages:
            # Fallback to keys if pages list is empty or doesn't exist as expected
            pages = [k for k in data.keys() if k != "pages"]

        return build_tree(pages)
    except Exception as e:
        return {"error": str(e)}

def flatten_hierarchy(tree):
    # Apply 3-click rule: flatten the structure
    # Current structure is often:
    # product-details -> product -> item.html
    # products -> collections -> category.html

    # We want:
    # / (home)
    # /products (list)
    # /products/[id] (details)
    # /collections/[id] (category)
    # /about, /contact, /science, etc.

    flattened = {
        "home": "/",
        "about": "/about",
        "contact": "/contact",
        "science": "/science",
        "services": "/services",
        "resources": "/resources",
        "products": {
            "index": "/products",
            "collections": {},
            "items": {}
        },
        "legal": {
            "shipping": "/shipping-policy",
            "refund": "/refund-policy",
            "copyright": "/copyright-policy",
            "medical-disclaimer": "/medical-disclaimer"
        }
    }

    # Logic to populate collections and items from the tree
    if "products" in tree and "collections" in tree["products"]:
        for coll in tree["products"]["collections"]:
            if coll.endswith(".html"):
                name = coll.replace(".html", "")
                if name != "index":
                    flattened["products"]["collections"][name] = f"/collections/{name}"

    if "product-details" in tree and "product" in tree["product-details"]:
        for item in tree["product-details"]["product"]:
            if item.endswith(".html"):
                name = item.replace(".html", "")
                flattened["products"]["items"][name] = f"/products/{name}"

    return flattened

if __name__ == "__main__":
    snapshot_file = "gathering/site_snapshot.json"
    if len(sys.argv) > 1:
        snapshot_file = sys.argv[1]

    current = get_current_hierarchy(snapshot_file)
    improved = flatten_hierarchy(current)

    result = {
        "current_hierarchy": current,
        "improved_hierarchy": improved
    }
    print(json.dumps(result, indent=2))
