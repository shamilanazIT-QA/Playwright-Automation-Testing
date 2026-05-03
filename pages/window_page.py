class WindowPage:
    def __init__(self, page):
        self.page = page
        self.click_here_link  = page.get_by_role("link", name="Click Here").click()
    def navigate(self):
        self.page.goto("https://the-internet.herokuapp.com/windows")
    def click_new_window(self, context):
        with context.expect_event("page") as new_page_info:
            self.click_here_link.click()
        return new_page_info.value

