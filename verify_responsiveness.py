from playwright.sync_api import sync_playwright
import os

def capture_screenshots():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Absolute path to the index.html file
        file_path = "file://" + os.path.abspath("index.html")

        # Desktop
        page.set_viewport_size({"width": 1280, "height": 800})
        page.goto(file_path)
        page.screenshot(path="screenshot_desktop.png", full_page=True)
        print("Desktop screenshot saved.")

        # Mobile
        page.set_viewport_size({"width": 375, "height": 667})
        page.goto(file_path)
        page.screenshot(path="screenshot_mobile.png", full_page=True)
        print("Mobile screenshot saved.")

        browser.close()

if __name__ == "__main__":
    capture_screenshots()
