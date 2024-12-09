from pages.base import Base
from data.constants import Constants
from Locators.main import Main
from data.assertions import Assertions
from playwright.sync_api import Page


class Main(Base):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.assertion = Assertions(page)


    def user_registration(self):
        self.open("/registration")
        pass