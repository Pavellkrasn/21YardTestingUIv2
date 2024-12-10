import time

from pages.base import Base
from data.constants import Constants
from Locators.application import Application
from data.assertions import Assertions
from playwright.sync_api import Page


class ApplicationPage(Base):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.assertion = Assertions(page)
        self.create_button = page.get_by_role(role = "button", name="Опубликовать")

    def fill_application(self):
        self.open("/applications/create")
        self.click(Application.INPUT_CATEGORY)
        self.page.get_by_text("Геология").click()
        self.page.keyboard.press("Enter")
        self.input(Application.INPUT_SCOPE_OF_WORK, "Тест Описание работ")
        self.click_enter(Application.INPUT_REGION)
        self.click_enter(Application.INPUT_CITY)
        self.wait_for_element(Application.INPUT_PRICE_DETAILS)
        self.input(Application.INPUT_PRICE_DETAILS, "Тест Описание цены")
        time.sleep(2)

    def end_create(self):
        self.create_button.click()
        self.wait_for_element(Application.APRUVE_NUMBER_PANEL)
        self.click(Application.APRUVE_NUMBER_PANEL_CANSEL_BUTTON)


       # self.click(Application.INPUT_CATEGORY)
application_coordinates = {
    "region": (500, 500),
    "category": (500, 350),
    "city": (500, 1000)
}

