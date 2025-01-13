import pytest

from pages.registration_page import OpenRegistrationPage


@pytest.mark.smoke
class TestLogin:
    def test_user_login(self, browser):
        (OpenRegistrationPage(browser, create_test_data=None)
        .fill_registration_fields()
        .click_on_checkboxes()
        .click_on_registration_button()
        .reset_password())
