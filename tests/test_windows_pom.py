import sys
import os
sys.path.append(os.getcwd()) # This tells Python to look in the current folder for your 'pages' folder

from playwright.sync_api import sync_playwright, expect  # Add 'expect' here
from pages.window_page import WindowPage

def test_multi_window():
    with sync_playwright() as p:
        is_ci = os.getenv("CI") == "true"
        browser = p.chromium.launch(headless=is_ci)
        context = browser.new_context()
        page = context.new_page()

        window_tester = WindowPage(page)
        window_tester.navigate()

        new_tab = window_tester.click_new_window(context)

        # --- THE ASSERTIONS ---
        # 1. Assert the title is correct
        expect(new_tab).to_have_title("New Window")

        # 2. Assert the header text on the new page
        header = new_tab.locator("h3")
        expect(header).to_have_text("New Window")

        print("Assertions passed successfully!")
        browser.close()


if __name__ == "__main__":
    test_multi_window()