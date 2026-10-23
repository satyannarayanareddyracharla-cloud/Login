import pytest
from playwright.sync_api import Browser, Page, sync_playwright


BASE_URL = "https://qapracticehub.com/#forms"


@pytest.fixture(scope="session")
def browser() -> Browser:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(channel="chrome", headless=False)
        yield browser
        browser.close()


@pytest.fixture
def forms_page(browser: Browser) -> Page:
    page = browser.new_page()
    page.goto(BASE_URL, wait_until="domcontentloaded")

    accept_cookies = page.get_by_role("button", name="Accept", exact=True)
    if accept_cookies.is_visible():
        accept_cookies.click()

    yield page
    page.close()
