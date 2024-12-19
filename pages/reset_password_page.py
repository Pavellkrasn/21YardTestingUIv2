import time

import pytest
from playwright.sync_api import expect
from playwright.sync_api import Page
from Locators.registration import Registration
from configuration.postgress_utils import confirm_user_email, is_user_email_confirmed, is_user_phone_confirmed, \
    confirm_user_phone
from data.bulder import UserDataBuilder
from data.constants import Constants
from data.decorators import retry_on_error
from fixtures.user_company_data import create_test_data
from pages.base import Base
from data.assertions import Assertions
import configuration.postgress_utils
from Locators.reset_password import ResetPassword
from settings import settings


class OpenResetPasswordPage(Base):
    def __init__(self, page: Page, create_test_data) -> None:
        super().__init__(page)
        self.assertion = Assertions(page)
        self.builder = UserDataBuilder()
        self.registration_data = self.builder.build()
        self.iS = ResetPassword()
        self.open("/resetPassword")


    def reset_password(self):

        self.input(self.iS.INPUT_RESET_PASSWORD, Constants.login)
        self.click(self.iS.BUTTON_RESET)
        self.route_abort(self.iS.RESET_PASSWORD_URL)
        self.assertions.check_URL("https://dev.21yard.com/resetPassword/checkEmail")
        return self


