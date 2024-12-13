import time

from playwright.sync_api import Page

from Locators.personal_account import PersonalAccount
from data.bulder import CreateCompanyBuilder
from data.assertions import Assertions
from pages.base import Base


class OpenPersonalAccountPage(Base):
    def __init__(self, page: Page):
        super().__init__(page)
        self.assertions = Assertions(page)
        self.builder = CreateCompanyBuilder()
        self.company_data = self.builder.build()
        self.create_button = self.page.get_by_role("button", name="Добавить компанию")
        self.frame = page.locator("div[class*='isOpen']")


    def delete_account(self):
        self.open("/personalAccount/profile")
        self.click(PersonalAccount.SETTINGS_BUTTON)
        self.click(PersonalAccount.DELETE_ACCOUNT_BUTTON)
        self.click(PersonalAccount.ACTUALY_DELETE)
        self.assertions.check_URL("https://dev.21yard.com/")
        return self

    def fill_company_fields(self):
        self.open("/personalAccount/profile")
        self.click(PersonalAccount.MY_COMPANIES_BUTTON)
        self.focus_press_by_locator(self.create_button,"Enter")
        self.wait_for_element("div[class*='isOpen']")
        self.input(PersonalAccount.WRAPPER_INPUT_COMPANY_NAME, self.company_data["company_name"])
        self.input(PersonalAccount.WRAPPER_INPUT_COMPANY_INN, self.company_data["inn"])
        return self

    def create_company(self):
        self.click(PersonalAccount.WRAPPER_BUTTON_CREATE_COMPANY)
        return self

    def checkNameAndInn(self):

        return self




