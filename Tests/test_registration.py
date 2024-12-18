import pytest

from fixtures.user_company_data import create_test_data
from pages.registration_page import OpenRegistrationPage


@pytest.mark.smoke
class TestRegistration():
    @pytest.mark.usefixtures('create_test_data')
    def test_user_registration(self, browser, create_test_data):
        (OpenRegistrationPage(browser, create_test_data)
         .fill_registration_fields(create_test_data)
         .click_on_checkboxes()
         .click_on_registration_button()
         .check_confirm_text_title())
