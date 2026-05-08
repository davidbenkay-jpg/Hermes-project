import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        # Use a persistent context to save login cookies later
        context = await browser.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
        page = await context.new_page()
        
        # Target URL for TAGRY Earbuds
        url = "https://www.amazon.com/s?k=TAGRY+Bluetooth+Headphones+True+Wireless+Earbuds+60H"
        
        print(f"Hermes is reaching out to: {url}")
        await page.goto(url)
        
        # Take a screenshot to prove we can see the item
        await page.screenshot(path="hermes_search_result.png")
        print("Screenshot saved as hermes_search_result.png")
        
        await browser.close()

asyncio.run(run())
