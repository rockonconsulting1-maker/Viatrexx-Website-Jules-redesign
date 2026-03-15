import json
import os
import subprocess

def check_redirects():
    print("Checking 301 Redirects...")
    result = subprocess.run(["python3", "verify_redirects.py"], capture_output=True, text=True)
    if "All redirect verifications PASSED" in result.stdout:
        return True, result.stdout
    return False, result.stdout

def check_validation_script():
    print("Checking Validation Scores...")
    result = subprocess.run(["python3", "skills/website-rebuilder-orchestrator/scripts/validate_full_site.py"], capture_output=True, text=True)
    try:
        data = json.loads(result.stdout)
        if data["performance"] >= 90 and data["best_practices"] >= 90:
            return True, data
    except:
        pass
    return False, result.stdout

def check_files():
    print("Checking Required Files...")
    required = [
        "rebuilt-site/next.config.js",
        "rebuilt-site/package.json",
        "rebuilt-site/app/globals.css",
        "rebuilt-site/components/layout/navbar.tsx",
        "rebuilt-site/components/layout/footer.tsx",
        "rebuilt-site/lib/utils.ts"
    ]
    missing = [f for f in required if not os.path.exists(f)]
    if not missing:
        return True, "All files present"
    return False, f"Missing files: {missing}"

def run_all():
    checks = {
        "Redirects": check_redirects(),
        "Validation": check_validation_script(),
        "File Consistency": check_files()
    }

    all_ok = True
    for name, (status, msg) in checks.items():
        icon = "✅" if status else "❌"
        print(f"{icon} {name}: {msg}")
        if not status:
            all_ok = False

    if all_ok:
        print("\n🚀 SITE IS READY FOR LAUNCH!")
    else:
        print("\n⚠️ LAUNCH READINESS FAILED.")
        exit(1)

if __name__ == "__main__":
    run_all()
