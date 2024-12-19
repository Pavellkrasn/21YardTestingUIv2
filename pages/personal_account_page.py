import pytest
from playwright.sync_api import Page
from configuration.postgress_utils import delete_applications, delete_companies
from Locators.personal_account import PersonalAccount
from data.bulder import CompanyDataBuilder
from data.assertions import Assertions
from data.decorators import retry_on_error
from fixtures.user_company_data import create_test_data
from pages.base import Base

@pytest.mark.usefixtures('create_test_data')
class OpenPersonalAccountPage(Base):
    def __init__(self, page: Page,create_test_data):
        super().__init__(page)
        self.assertions = Assertions(page)
        self.builder = CompanyDataBuilder()
        self.company_data = self.builder.build()
        self.create_button = self.page.get_by_role("button", name="Добавить компанию")
        self.frame = page.locator("div[class*='isOpen']")
        self.test_data = create_test_data


    def delete_account(self,create_test_data: dict):
        self.open("/personalAccount/profile")
        self.click(PersonalAccount.SETTINGS_BUTTON)
        self.click(PersonalAccount.DELETE_ACCOUNT_BUTTON)
        self.click(PersonalAccount.ACTUALY_DELETE)
        delete_applications("Тест Описание работ")
        delete_companies(create_test_data['email'])
        self.assertions.check_URL("")
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

    def check_name_and_inn(self):
        self.assertions.is_element_present(PersonalAccount.MY_COMPANY)
        self.assertions.have_text(PersonalAccount.MY_COMPANY_NAME_TITLE,self.company_data['company_name'])
        self.assertions.have_text(PersonalAccount.MY_COMPANY_INN_TITLE, f"ИНН: {self.company_data['inn']}")
        return self




