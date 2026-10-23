from playwright.sync_api import Locator, Page


class RegistrationPage:
    def __init__(self, page: Page) -> None:
        self._page = page
        self._first_name = page.get_by_test_id("reg-firstname")
        self._last_name = page.get_by_test_id("reg-lastname")
        self._email = page.get_by_test_id("reg-email")
        self._country = page.get_by_test_id("reg-country")
        self._register_button = page.get_by_role(
            "button", name="Register", exact=True
        )
        self._clear_button = page.get_by_role("button", name="Clear", exact=True)

    def register(
        self, first_name: str, last_name: str, email: str, country: str
    ) -> None:
        self._first_name.fill(first_name)
        self._last_name.fill(last_name)
        self._email.fill(email)
        self._country.select_option(label=country)
        self._register_button.click()

    def submit_empty(self) -> None:
        self._register_button.click()

    def required_fields_missing(self) -> dict[str, bool]:
        return {
            "first_name": self._first_name.evaluate(
                "(input) => input.validity.valueMissing"
            ),
            "last_name": self._last_name.evaluate(
                "(input) => input.validity.valueMissing"
            ),
            "email": self._email.evaluate(
                "(input) => input.validity.valueMissing"
            ),
            "country": self._country.evaluate(
                "(input) => input.validity.valueMissing"
            ),
        }

    def email_is_valid(self) -> bool:
        return self._email.evaluate("(input) => input.validity.valid")

    def has_success_message(self, first_name: str, last_name: str) -> bool:
        message: Locator = self._page.get_by_text(
            f"Registration successful for {first_name} {last_name}!", exact=True
        )
        return message.is_visible()

    def clear(self) -> None:
        self._clear_button.click()

    def field_values(self) -> dict[str, str]:
        return {
            "first_name": self._first_name.input_value(),
            "last_name": self._last_name.input_value(),
            "email": self._email.input_value(),
            "country": self._country.input_value(),
        }
