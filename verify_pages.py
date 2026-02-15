import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # Get absolute path to index.html
        path = os.path.abspath("index.html")
        url = f"file://{path}"

        print(f"Opening {url}")

        # Desktop
        await page.set_viewport_size({"width": 1280, "height": 800})
        await page.goto(url)
        # Wait a bit for animations/styles
        await asyncio.sleep(2)
        await page.screenshot(path="desktop_screenshot.png", full_page=True)
        print("Desktop screenshot saved.")

        # Mobile
        await page.set_viewport_size({"width": 375, "height": 667})
        await page.goto(url)
        # Wait a bit for animations/styles
        await asyncio.sleep(2)
        await page.screenshot(path="mobile_screenshot.png", full_page=True)
        print("Mobile screenshot saved.")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
