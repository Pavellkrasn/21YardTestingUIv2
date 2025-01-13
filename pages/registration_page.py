import pytest
from playwright.sync_api import expect
from playwright.sync_api import Page

from Locators.registration import Registration
from Locators.reset_password import ResetPassword
from configuration.postgress_utils import confirm_user_email, is_user_email_confirmed, is_user_phone_confirmed, \
    confirm_user_phone
from data.bulder import UserDataBuilder
from fixtures.user_company_data import create_test_data
from pages.base import Base
from data.assertions import Assertions


@pytest.mark.usefixtures('create_test_data')
class OpenRegistrationPage(Base):
    def __init__(self, page: Page, create_test_data = None) -> None:
        super().__init__(page)
        self.assertion = Assertions(page)
        self.builder_user_data = UserDataBuilder().build()  # Инициализация билдера для независимых тестов
        self.fixture_user_data = create_test_data
        self.user_name = self.fixture_user_data["name"] if create_test_data else self.builder_user_data["name"]
        self.user_email = self.fixture_user_data["email"] if create_test_data else self.builder_user_data["email"]
        self.user_phone = self.fixture_user_data["phone"]if create_test_data else self.builder_user_data["phone"]
        self.user_password = self.fixture_user_data["password"]if create_test_data else self.builder_user_data["password"]


    def fill_registration_fields(self,email = None):
        self.open("/registration")
        self.page.wait_for_timeout(1000)
        self.input(Registration.INPUT_FIRSTNAME, self.user_name)
        self.input(Registration.INPUT_EMAIL, email or self.user_email)
        self.input(Registration.INPUT_PHONE, self.user_phone)
        self.input(Registration.INPUT_PASSWORD, self.user_password)
        self.input(Registration.INPUT_REP_PASS, self.user_password)
        return self

    def click_on_checkboxes(self):
        self.click(Registration.SERVICE_CHECKBOX)
        self.click(Registration.OFERTA_CHECKBOX)
        self.click(Registration.KONF_CHECKBOX)
        return self

    def click_on_registration_button(self):
        self.click(Registration.REGISTRATION_BUTTON)
        self.page.wait_for_timeout(1000)
        self.assertion.check_URL("registration/confirm")
        return self

    def confirm_phone(self,  email = None):
        confirm_user_phone(email or self.user_email)
        assert is_user_phone_confirmed(email or self.user_email)
        return self

    def confirm_email(self, email = None):
        confirm_user_email(email or self.user_email)
        assert is_user_email_confirmed(email or self.user_email)

        return self

    def check_confirm_text_title(self):
        self.page.wait_for_url("https://dev.21yard.com/registration/confirm")
        expect(self.page.locator(Registration.CONFIRM_TEXT_SUBTITLE)).to_contain_text(self.user_email)

    def reset_password(self):
        self.open("/resetPassword")
        self.input(ResetPassword.INPUT_RESET_PASSWORD,self.user_email)
        self.click(ResetPassword.BUTTON_RESET)
        self.route_abort(ResetPassword.RESET_PASSWORD_URL)
        self.assertion.check_URL("resetPassword/checkEmail")
        return self











