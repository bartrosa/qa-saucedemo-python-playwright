import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def playwright_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        yield context
        context.close()
        browser.close()

@pytest.fixture(scope="session")
def page(playwright_context):
    page = playwright_context.new_page()
    yield page
    page.close()
