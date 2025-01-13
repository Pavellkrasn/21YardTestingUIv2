import pytest

from data.bulder import UserDataBuilder
from data.decorators import retry_on_error
from pages.base import Base
import time
from data.constants import Constants
from Locators.auth import Auth
from data.assertions import Assertions
from playwright.sync_api import Page
refresh_token = ""
@pytest.mark.usefixtures('create_test_data')
class OpenLoginPage(Base):
    def __init__(self, page: Page, create_test_data) -> None:
        super().__init__(page)
        self.assertion = Assertions(page)
        self.builder_company_data = UserDataBuilder().build()
        self.fixture_user_data = create_test_data
        self.user_email = self.fixture_user_data['email'] if create_test_data else Constants.login
        self.user_password = self.fixture_user_data['password']if create_test_data else Constants.password


    def user_login(self, constants_email = None):
        self.open("/login")
        self.page.wait_for_timeout(800)
        self.input(Auth.INPUT_EMAIL, constants_email or self.user_email)
        self.input(Auth.INPUT_PASSWORD,self.user_password)
        self.click(Auth.BUTTON_LOGIN)
        self.assertion.check_URL("")
        return self


