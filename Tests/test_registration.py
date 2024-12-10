import pytest
from pages.registration_page import OpenRegistrationPage


@pytest.mark.smoke
class TestLogin:
    def test_user_registration(self, browser):
        (OpenRegistrationPage(browser)
         .fill_registration_fields()
         .clickOnCheckboxes()
         .clickOnRegistrationButton()
         .checkConfirmTextTitle())
