#!/usr/bin/env python3
import sys, json
def generate_redirects(tree_diff):
    # Logic to generate 301 redirects
    return [{"from": "/old-path", "to": "/new-path", "type": 301}]
if __name__ == "__main__":
    print(json.dumps(generate_redirects({}), indent=2))
