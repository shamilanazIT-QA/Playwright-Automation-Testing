from playwright.sync_api import sync_playwright


def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context= browser.new_context()
        page= context.new_page()

        # 1. Go to a practice site with a "multiple windows" link
        page.goto("https://the-internet.herokuapp.com/windows")

        # 2. Start waiting for the new tab to open BEFORE you click
        with context.expect_event("page") as new_page_info:
            page.get_by_role("link", name="Click Here").click()

        # 3. Assign the new tab to a variable
        new_tab = new_page_info.value

        # 4. Interact with the NEW tab
        new_tab.wait_for_load_state()
        print(f"New Tab Title: {new_tab.title()}")
        print(f"New Tab Text: {new_tab.locator('h3').inner_text()}")

        # 5. Switch back to the ORIGINAL tab and do something
        page.bring_to_front()
        print(f"Original Tab Title: {page.title()}")

        browser.close()


run()