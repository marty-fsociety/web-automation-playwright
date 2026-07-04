
import asyncio


from playwright.async_api import async_playwright



async def main() -> None:
    
    async with async_playwright() as playwright:
        
        browser = await playwright.chromium.launch(headless=False)

        
        context = await browser.new_context()

        
        page = await context.new_page()

        
        await page.goto("https://www.wikipedia.org")
        
        await page.fill('input[name="search"]', "Python")
        
        await page.press('input[name="search"]', "Enter")
        
        await page.wait_for_load_state("networkidle")
        
        await page.screenshot(path="wikipedia_python.png")
        
        await asyncio.sleep(10)
        
        await browser.close()




if __name__ == "__main__":
    asyncio.run(main())
