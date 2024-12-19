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
        self.test_data = create_test_data


    def user_login(self, create_test_data=None):
        self.open("/login")
        self.page.wait_for_timeout(800)
        self.input(Auth.INPUT_EMAIL, self.test_data['email'] if create_test_data else Constants.login )
        self.page.pause()
        self.input(Auth.INPUT_PASSWORD, self.test_data['password']if create_test_data else Constants.password)
        self.click(Auth.BUTTON_LOGIN)
        self.assertion.check_URL("")
        return self


