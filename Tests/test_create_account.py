import pytest

from data.constants import Constants
from pages.personal_account_page import OpenPersonalAccountPage
from pages.registration_page import OpenRegistrationPage

@pytest.mark.skip("Аккаунт создается один раз после чистки бд")
class TestCreateAccount:
    def test_create_account(self, browser):
        (OpenRegistrationPage(browser)
         .fill_registration_fields(email=Constants.login)
         .click_on_checkboxes()
         .click_on_registration_button()
         .confirm_email(email=Constants.login)
         .confirm_phone())
        (OpenPersonalAccountPage(browser)
         .fill_company_fields()
         .create_company()
         .check_name_and_inn())
