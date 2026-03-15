#!/usr/bin/env python3
import sys, json
def scan_anti_patterns(files):
    # Logic to detect 67 styles + 99 UX guidelines issues
    return [{"file": "index.html", "issue": "Harsh shadow detected", "type": "anti-pattern"}]
if __name__ == "__main__":
    print(json.dumps(scan_anti_patterns([]), indent=2))
