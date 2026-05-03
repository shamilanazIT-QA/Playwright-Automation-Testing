import sys
import os
sys.path.append(os.getcwd()) # This tells Python to look in the current folder for your 'pages' folder

from playwright.sync_api import sync_playwright
from pages.window_page import WindowPage

def test_multi_window():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context= browser.new_context()
        page= context.new_page()
        # Use the Page Object

        window_tester = WindowPage(page)
        window_tester.navigate()

        new_tab = window_tester.click_new_window(context)

        # 4. Interact with the NEW tab
        print(f"New Tab Title: {new_tab.title()}")
        print(f"New Tab Text: {new_tab.locator('h3').inner_text()}")

        # 5. Switch back to the ORIGINAL tab and do something
        page.bring_to_front()
        print(f"Original Tab Title: {page.title()}")

        browser.close()


test_multi_window()