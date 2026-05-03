class WindowPage:
    def __init__(self, page):
        self.page = page
        # ONLY define the locator here. Do NOT add .click() at the end.
        self.click_here_link = page.get_by_role("link", name="Click Here")

    def navigate(self):
        self.page.goto("https://the-internet.herokuapp.com/windows")

    def click_new_window(self, context):
        # Now we perform the click here, AFTER navigation has happened
        with context.expect_event("page") as new_page_info:
            self.click_here_link.click()
        return new_page_info.value

