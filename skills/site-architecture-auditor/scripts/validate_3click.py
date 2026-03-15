#!/usr/bin/env python3
import sys
import json

def get_depth(node, current_depth=0):
    if not isinstance(node, dict) or not node:
        return current_depth

    max_d = current_depth
    for key, value in node.items():
        d = get_depth(value, current_depth + 1)
        if d > max_d:
            max_d = d
    return max_d

def find_deep_paths(node, path="", current_depth=0):
    offenders = []
    if current_depth > 3:
        offenders.append(path)

    if isinstance(node, dict):
        for key, value in node.items():
            new_path = f"{path}/{key}" if path else key
            offenders.extend(find_deep_paths(value, new_path, current_depth + 1))

    return offenders

def validate_3click(hierarchy):
    depth = get_depth(hierarchy)
    offenders = find_deep_paths(hierarchy)

    return {
        "max_depth": depth,
        "is_valid": depth <= 3,
        "offenders": offenders
    }

if __name__ == "__main__":
    try:
        if len(sys.argv) > 1:
            with open(sys.argv[1], 'r') as f:
                data = json.load(f)
        else:
            # Expecting input from stdin if no file provided
            data = json.load(sys.stdin)

        # If it's the full audit output, extract improved_hierarchy
        hierarchy = data.get("improved_hierarchy", data)

        result = validate_3click(hierarchy)
        print(json.dumps(result, indent=2))
    except Exception as e:
        print(json.dumps({"error": str(e)}, indent=2))
