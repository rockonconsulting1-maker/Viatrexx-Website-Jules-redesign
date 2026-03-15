#!/usr/bin/env python3
import sys
import json
import subprocess

def run_script(script_path, input_file=None, stdin_data=None):
    cmd = ["python3", script_path]
    if input_file:
        cmd.append(input_file)

    process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate(input=stdin_data)

    if process.returncode != 0:
        return {"error": stderr}
    return json.loads(stdout)

def generate_ascii_tree(node, prefix="", is_last=True):
    tree_str = ""
    if isinstance(node, dict):
        keys = sorted(node.keys())
        for i, key in enumerate(keys):
            marker = "└── " if i == len(keys) - 1 else "├── "
            tree_str += f"{prefix}{marker}{key}\n"
            new_prefix = prefix + ("    " if i == len(keys) - 1 else "│   ")
            tree_str += generate_ascii_tree(node[key], new_prefix, i == len(keys) - 1)
    return tree_str

def generate_mermaid(hierarchy):
    mermaid = "graph TD\n"
    mermaid += "  Home[/]\n"

    # Core pages
    core_pages = ["About", "Contact", "Science", "Services", "Resources", "Products", "Legal"]
    for page in core_pages:
        mermaid += f"  Home --> {page}\n"

    # Nested pages
    if "products" in hierarchy:
        mermaid += "  Products --> Collections[Collections/Categories]\n"
        mermaid += "  Products --> Items[Product Details]\n"

    if "legal" in hierarchy:
        for key in hierarchy["legal"]:
            mermaid += f"  Legal --> {key.capitalize()}\n"

    return mermaid

if __name__ == "__main__":
    snapshot = "gathering/site_snapshot.json"

    hierarchy_data = run_script("skills/site-architecture-auditor/scripts/audit_hierarchy.py", snapshot)
    redirects = run_script("skills/site-architecture-auditor/scripts/generate_redirects.py", snapshot)
    validation = run_script("skills/site-architecture-auditor/scripts/validate_3click.py", stdin_data=json.dumps(hierarchy_data))

    ascii_tree = generate_ascii_tree(hierarchy_data["improved_hierarchy"])
    mermaid_diag = generate_mermaid(hierarchy_data["improved_hierarchy"])

    final_audit = {
        "ascii_tree": ascii_tree,
        "mermaid": mermaid_diag,
        "redirects": redirects,
        "validation": validation,
        "improved_hierarchy": hierarchy_data["improved_hierarchy"]
    }

    print(json.dumps(final_audit, indent=2))
