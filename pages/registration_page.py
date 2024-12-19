import time

import pytest
from playwright.sync_api import expect
from playwright.sync_api import Page
from Locators.registration import Registration
from configuration.postgress_utils import confirm_user_email, is_user_email_confirmed, is_user_phone_confirmed, \
    confirm_user_phone
from data.bulder import UserDataBuilder
from data.decorators import retry_on_error
from fixtures.user_company_data import create_test_data
from pages.base import Base
from data.assertions import Assertions
import configuration.postgress_utils


@pytest.mark.usefixtures('create_test_data')
class OpenRegistrationPage(Base):
    def __init__(self, page: Page, create_test_data) -> None:
        super().__init__(page)
        self.assertion = Assertions(page)
        self.test_data = create_test_data # фикстура для e2e
        self.builder = UserDataBuilder()  # Инициализация билдера для независимых тестов
        self.registration_data = self.builder.build()  # Генерация данных сразу при инициализации

    def fill_registration_fields(self,create_test_data = None):
        self.open("/registration")
        self.page.wait_for_timeout(800)
        self.input(Registration.INPUT_FIRSTNAME,self.test_data["name"] if create_test_data else self.registration_data["name"])
        self.input(Registration.INPUT_EMAIL,self.test_data["email"]if create_test_data else self.registration_data["email"])
        self.input(Registration.INPUT_PHONE,self.test_data["phone"]if create_test_data else self.registration_data["phone"] )
        self.input(Registration.INPUT_PASSWORD,self.test_data["password"]if create_test_data else self.registration_data["password"])
        self.input(Registration.INPUT_REP_PASS,self.test_data["password"]if create_test_data else self.registration_data["password"])
        return self

    def click_on_checkboxes(self):
        self.click(Registration.SERVICE_CHECKBOX)
        self.click(Registration.OFERTA_CHECKBOX)
        self.click(Registration.KONF_CHECKBOX)
        return self

    def click_on_registration_button(self, create_test_data = None):

        self.click(Registration.REGISTRATION_BUTTON)
        confirm_user_email(self.test_data["email"])
        confirm_user_phone(self.test_data["email"])
        return self

            # Тест часто падает по причине бага, но не понятно чьего.
            # Если быстрый ввод символов идет в ряд инпутов часто
            # первый инпут просто стирается

    def check_confirm_text_title(self):
        self.page.wait_for_url("https://dev.21yard.com/registration/confirm")
        print(is_user_phone_confirmed(self.test_data['email']))
        print(is_user_email_confirmed(self.test_data['email']))
        print(self.test_data['email'])
        assert is_user_email_confirmed(self.test_data['email'])
        assert is_user_phone_confirmed(self.test_data['email'])
        expected_email = self.test_data['email'] if self.test_data['email'] else self.registration_data['email']
        expect(self.page.locator(Registration.CONFIRM_TEXT_SUBTITLE)).to_contain_text(expected_email) # Проверяем что в тексте есть наш емейл











