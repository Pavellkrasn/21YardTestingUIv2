import time
from playwright.sync_api import expect
from playwright.sync_api import Page, Playwright

from Locators.registration import Registration
from data.bulder import RegistrationDataBuilder
from pages.base import Base
from data.assertions import Assertions


class OpenRegistrationPage(Base):
    def __init__(self,page: Page) -> None:
        super().__init__(page)
        self.assertion = Assertions(page)
        self.builder = RegistrationDataBuilder()  # Инициализация билдера
        self.registration_data = self.builder.build()  # Генерация данных сразу при инициализации

    def fill_registration_fields(self):
        self.open("/registration")
        # self.page.pause()
        self.input(Registration.INPUT_FIRSTNAME,self.registration_data["name"])
        self.input(Registration.INPUT_EMAIL,self.registration_data["email"])
        self.input(Registration.INPUT_PHONE,self.registration_data["phone"])
        self.input(Registration.INPUT_PASSWORD,self.registration_data["password"])
        self.input(Registration.INPUT_REP_PASS,self.registration_data["password"])
        return self

    def clickOnCheckboxes(self):
        self.click(Registration.SERVICE_CHECKBOX)
        self.click(Registration.OFERTA_CHECKBOX)
        self.click(Registration.KONF_CHECKBOX)
        return self

    def clickOnRegistrationButton(self):
        self.click(Registration.REGISTRATION_BUTTON)
        return self

    def checkConfirmTextTitle(self):
        self.page.wait_for_url("https://dev.21yard.com/registration/confirm")
        (expect(self.page.locator(Registration.CONFIRM_TEXT_SUBTITLE))
         .to_contain_text(self.registration_data['email'])) # Проверяем что в тексте есть наш емейл











