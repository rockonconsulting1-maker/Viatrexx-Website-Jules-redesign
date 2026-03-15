#!/usr/bin/env python3
import sys, json
def rewrite_section(old_text, design_md, audience):
    # Benefit-driven rewrite
    new = old_text.replace("We do X", "You get Y in 30 days")
    return {"new_copy": new, "rationale": "clarity + specificity"}

if __name__ == "__main__":
    print(json.dumps({"status": "ready"}, indent=2))
