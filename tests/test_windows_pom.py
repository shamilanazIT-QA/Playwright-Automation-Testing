import sys
import os
sys.path.append(os.getcwd()) # This tells Python to look in the current folder for your 'pages' folder

from playwright.sync_api import sync_playwright
from pages.window_page import WindowPage


def test_multi_window():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # Ensure headless for GitHub
        context = browser.new_context()
        page = context.new_page()

        # 1. Create the object (This now just stores the locators)
        window_tester = WindowPage(page)

        # 2. Navigate (This puts the buttons on the screen)
        window_tester.navigate()

        # 3. Click (Now Playwright can actually find the link!)
        new_tab = window_tester.click_new_window(context)

        print(f"New tab title: {new_tab.title()}")
        browser.close()

test_multi_window()