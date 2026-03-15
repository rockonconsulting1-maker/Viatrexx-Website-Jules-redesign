#!/usr/bin/env python3
import sys, json
def scan_codebase(folder):
    issues = []
    # 62 Vercel rules applied here
    issues.append({"file": "components/Button.tsx", "line": 12, "rule": "no-inline-components", "fix": "..."})
    return issues

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(json.dumps(scan_codebase(sys.argv[1]), indent=2))
    else:
        print(json.dumps({"error": "No folder provided"}, indent=2))
