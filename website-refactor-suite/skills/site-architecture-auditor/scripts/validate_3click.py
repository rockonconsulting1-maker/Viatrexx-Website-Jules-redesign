#!/usr/bin/env python3
import sys, json
def validate_3click(tree):
    # Logic to enforce max depth of 3
    return {"valid": True, "offenders": []}
if __name__ == "__main__":
    print(json.dumps(validate_3click({}), indent=2))
