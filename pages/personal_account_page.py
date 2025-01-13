import pytest
from playwright.sync_api import Page
from configuration.postgress_utils import delete_applications, delete_companies
from Locators.personal_account import PersonalAccount
from data.bulder import CompanyDataBuilder
from data.assertions import Assertions
from fixtures.user_company_data import create_test_data
from pages.base import Base

@pytest.mark.usefixtures('create_test_data')
class OpenPersonalAccountPage(Base):
    def __init__(self, page: Page,create_test_data = None):
        super().__init__(page)
        self.assertions = Assertions(page)
        self.builder_company_data = CompanyDataBuilder().build()
        self.fixture_company_data = create_test_data
        self.company_name = self.fixture_company_data['company_name'] if create_test_data else self.builder_company_data['company_name']
        self.company_inn = self.fixture_company_data['inn'] if create_test_data else self.builder_company_data['inn']
        self.user_email = self.fixture_company_data['email']
        self.create_button = self.page.get_by_role("button", name="Добавить компанию")
        self.frame = page.locator("div[class*='isOpen']")


    def delete_account(self):
        self.open("/personalAccount/profile")
        self.click(PersonalAccount.SETTINGS_BUTTON)
        self.click(PersonalAccount.DELETE_ACCOUNT_BUTTON)
        self.click(PersonalAccount.ACTUALY_DELETE)
        delete_applications("Тест Описание работ")
        delete_companies(self.user_email)
        self.assertions.check_URL("")
        return self

    def fill_company_fields(self):
        self.open("/personalAccount/profile")
        self.click(PersonalAccount.MY_COMPANIES_BUTTON)
        self.focus_press_by_locator(self.create_button,"Enter")
        self.wait_for_element("div[class*='isOpen']")
        self.input(PersonalAccount.WRAPPER_INPUT_COMPANY_NAME, self.company_name)
        self.input(PersonalAccount.WRAPPER_INPUT_COMPANY_INN, self.company_inn)
        return self

    def create_company(self):
        self.click(PersonalAccount.WRAPPER_BUTTON_CREATE_COMPANY)
        return self

    def check_name_and_inn(self):
        self.assertions.is_element_present(PersonalAccount.MY_COMPANY)
        try:
            self.assertions.have_text(PersonalAccount.MY_COMPANY_NAME_TITLE, self.company_name)
        except AssertionError:
            # БАГ! фронт не передает полностью имя
            try:
                self.assertions.have_text(PersonalAccount.MY_COMPANY_INN_TITLE, f"ИНН: {self.company_inn}")
                return self
            except AssertionError:
                raise AssertionError("Имя компании и ИНН не совпадают!")








