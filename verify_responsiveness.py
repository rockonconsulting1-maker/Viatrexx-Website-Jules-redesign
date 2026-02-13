import asyncio
from playwright.async_api import async_playwright
import os

async def capture_screenshots(url, page_name):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context()
        page = await context.new_page()

        # Resolve absolute path for local file
        abs_path = f"file://{os.path.abspath(url)}"

        # Desktop
        await page.set_viewport_size({"width": 1280, "height": 720})
        await page.goto(abs_path)
        await page.screenshot(path=f"screenshot_{page_name}_desktop.png")

        # Mobile
        await page.set_viewport_size({"width": 375, "height": 667})
        await page.goto(abs_path)
        # Wait a bit for animations
        await asyncio.sleep(1)
        await page.screenshot(path=f"screenshot_{page_name}_mobile.png")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(capture_screenshots("index.html", "index"))
    print("Screenshots captured.")
