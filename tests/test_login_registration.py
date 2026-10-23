from playwright.sync_api import Page

from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage


def test_login_with_valid_credentials(forms_page: Page) -> None:
    login_page = LoginPage(forms_page)

    login_page.login("tester", "password123")

    assert login_page.has_success_message("tester")


def test_login_rejects_invalid_credentials(forms_page: Page) -> None:
    login_page = LoginPage(forms_page)

    login_page.login("tester", "incorrect")

    assert login_page.has_invalid_credentials_message()


def test_login_requires_username_and_password(forms_page: Page) -> None:
    login_page = LoginPage(forms_page)

    login_page.submit_empty()

    assert login_page.required_fields_missing() == {
        "username": True,
        "password": True,
    }


def test_login_password_visibility_toggle(forms_page: Page) -> None:
    login_page = LoginPage(forms_page)

    assert login_page.password_type() == "password"
    login_page.toggle_password_visibility()
    assert login_page.password_type() == "text"
    login_page.toggle_password_visibility()
    assert login_page.password_type() == "password"


def test_registration_with_valid_details(forms_page: Page) -> None:
    registration_page = RegistrationPage(forms_page)

    registration_page.register(
        "Test", "User", "qa.automation@example.com", "India"
    )

    assert registration_page.has_success_message("Test", "User")


def test_registration_requires_all_fields(forms_page: Page) -> None:
    registration_page = RegistrationPage(forms_page)

    registration_page.submit_empty()

    assert registration_page.required_fields_missing() == {
        "first_name": True,
        "last_name": True,
        "email": True,
        "country": True,
    }
    assert not registration_page.has_success_message("", "")


def test_registration_currently_accepts_invalid_email(forms_page: Page) -> None:
    registration_page = RegistrationPage(forms_page)

    registration_page.register("Test", "User", "not-an-email", "India")

    assert not registration_page.email_is_valid()
    assert registration_page.has_success_message("Test", "User")


def test_registration_clear_resets_all_fields(forms_page: Page) -> None:
    registration_page = RegistrationPage(forms_page)
    registration_page.register(
        "Test", "User", "qa.automation@example.com", "India"
    )

    registration_page.clear()

    assert registration_page.field_values() == {
        "first_name": "",
        "last_name": "",
        "email": "",
        "country": "",
    }
