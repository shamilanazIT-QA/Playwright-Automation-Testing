from playwright.sync_api import sync_playwright


def run():
    with sync_playwright() as p:
        # slow_mo: puts a delay between actions so Google doesn't freak out
        browser = p.chromium.launch(headless=True, slow_mo=500)

        # Using a fake User Agent makes us look like a normal Chrome user
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
        context = browser.new_context(user_agent=user_agent)
        page = context.new_page()

        # Direct search URL often bypasses the main search bar's bot check
        page.goto("https://www.google.com/search?q=weather+in+London")

        # Check if Google is asking for cookies
        if page.get_by_role("button", name="Accept all").is_visible():
            page.get_by_role("button", name="Accept all").click()

        try:
            # Wait for the temperature element (using a more generic selector)
            page.wait_for_selector("[id='wob_tm']", timeout=10000)
            temp = page.inner_text("[id='wob_tm']")
            print(f"Success! The temperature is: {temp}°C")
        except:
            print("Google blocked us with a CAPTCHA. Try closing the browser and running again in 2 minutes.")
            page.screenshot(path="blocked.png")

        browser.close()


run()