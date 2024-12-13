from pages.base import Base
import time
from data.constants import Constants
from Locators.auth import Auth
from data.assertions import Assertions
from playwright.sync_api import Page


class Login(Base):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.assertion = Assertions(page)

    def user_login(self):
        self.open("/login")
        self.input(Auth.INPUT_EMAIL, Constants.login)
        self.input(Auth.INPUT_PASSWORD, Constants.password)
        self.click(Auth.BUTTON_LOGIN)
        self.assertion.check_URL("")
        return self



