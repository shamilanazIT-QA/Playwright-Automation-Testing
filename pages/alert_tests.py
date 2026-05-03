from playwright.sync_api import sync_playwright


def handle_alerts():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://the-internet.herokuapp.com/javascript_alerts")

        # 1. Setup the listener BEFORE triggering the alert
        # This tells Playwright to automatically click "OK"
        page.on("dialog", lambda dialog: dialog.accept())

        # 2. Click the button that triggers a simple Alert
        page.get_by_role("button", name="Click for JS Alert").click()

        # 3. Handling a "Confirm" alert (OK/Cancel) and sending text
        # We can change the listener to type into a prompt
        page.on("dialog", lambda dialog: dialog.accept("Hello from Playwright!"))
        page.get_by_role("button", name="Click for JS Prompt").click()

        # Verify the result text on the page
        result = page.locator("#result").inner_text()
        print(f"Action result: {result}")

        browser.close()


handle_alerts()