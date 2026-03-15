#!/usr/bin/env python3
import sys, json
def convert_component(old_code, design_tokens):
    # Replaces old classes with Tailwind + shadcn
    new_code = old_code.replace("className='old'", "className='shadcn-button'")
    return new_code

if __name__ == "__main__":
    print(json.dumps({"status": "ready"}, indent=2))
