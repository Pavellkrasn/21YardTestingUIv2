from pages.base import Base
from data.constants import Constants
from Locators.main import Main
from data.assertions import Assertions
from playwright.sync_api import Page


class OpenMainPage(Base):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.assertion = Assertions(page)


    def checker_main_page(self):
        self.open('')
        self.page.pause()
        self.assertion.check_presence(Main.WRAPPER_HEADLESS_MENU)
        self.assertion.check_presence(Main.TITLE_MAIN)
        self.assertion.check_presence(Main.TITLE_PARTNER_SECTOR)
        self.assertion.check_presence(Main.LIST_OF_COMPANIES_PARTNERS_DOCUMENT)
        self.assertion.check_presence(Main.LIST_OF_COMPANIES_PARTNERS_LOGO)
        self.assertion.check_presence(Main.LIST_OF_COMPANIES_PARTNERS_DOCUMENT)
        self.assertion.check_presence(Main.LIST_OF_REGISTRATION_AND_APPLICATION_BUTTONS_ON_MAIN_PAGE)
        self.assertion.check_presence(Main.LIST_OF_REGISTRATION_BUTTONS_ON_MAIN_PAGE)
        self.assertion.check_presence(Main.LIST_OF_APPLICATIONS_BUTTONS_ON_MAIN_PAGE)
        self.assertion.check_presence(Main.BUTTON_REGISTRATION_HEADLESS)
        self.assertion.check_presence(Main.BUTTON_LOGIN_HEADLESS)
        self.assertion.check_presence(Main.BUTTON_HEADLESS_MENU)



