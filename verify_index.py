import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # Open the local file
        # Since http.server might be slow to start, we can try to open the file directly or use localhost
        try:
            await page.goto('http://localhost:3000/index.html')
            await page.wait_for_load_state('networkidle')
            await page.screenshot(path='design_verification_index.png', full_page=True)
            print("Screenshot saved to design_verification_index.png")
        except Exception as e:
            print(f"Error during visual check: {e}")

        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
