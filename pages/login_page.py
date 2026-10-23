from typing import Optional

from playwright.sync_api import Locator, Page


class LoginPage:
    def __init__(self, page: Page) -> None:
        self._page = page
        self._username = page.get_by_test_id("login-username")
        self._password = page.get_by_test_id("login-password")
        self._password_toggle = page.get_by_test_id("login-password-toggle")
        self._login_button = page.get_by_role("button", name="Login", exact=True)

    def login(self, username: str, password: str) -> None:
        self._username.fill(username)
        self._password.fill(password)
        self._login_button.click()

    def submit_empty(self) -> None:
        self._login_button.click()

    def required_fields_missing(self) -> dict[str, bool]:
        return {
            "username": self._username.evaluate(
                "(input) => input.validity.valueMissing"
            ),
            "password": self._password.evaluate(
                "(input) => input.validity.valueMissing"
            ),
        }

    def toggle_password_visibility(self) -> None:
        self._password_toggle.click()

    def password_type(self) -> Optional[str]:
        return self._password.get_attribute("type")

    def has_success_message(self, username: str) -> bool:
        message: Locator = self._page.get_by_text(
            f"Login successful! Welcome, {username}.", exact=True
        )
        return message.is_visible()

    def has_invalid_credentials_message(self) -> bool:
        message = self._page.get_by_text(
            "Invalid credentials. Try username: tester, password: password123",
            exact=True,
        )
        return message.is_visible()
