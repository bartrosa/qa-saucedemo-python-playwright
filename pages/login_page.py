from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self):
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username: str, password: str):
        self.page.fill("input[name='user-name']", username)
        self.page.fill("input[name='password']", password)
        self.page.click("input[name='login-button']")
    
    def get_error_message(self):
        return self.page.text_content("h3[data-test='error']")
