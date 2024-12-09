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

    def press_arrow_down_and_enter(self) -> None:
        """
        Функция для имитации нажатий стрелки вниз и клавиши Enter.
        """
        # Нажимаем стрелку вниз num_down р
        self.page.keyboard.press("ArrowDown")
        time.sleep(1)
        self.page.keyboard.press("Enter")

    def some_def(self):
        self.open("/applications/create")
        self.click(Application.INPUT_REGION)
        self.press_arrow_down_and_enter()
        time.sleep(1)
        self.click(Application.INPUT_CITY)
        self.press_arrow_downсв юю_and_enter()
        self.click(Application.INPUT_CATEGORY)
        self.page.get_by_text("Геология").click()
        self.input(Application.INPUT_SCOPE_OF_WORK, "Нормальный обьем работ")
        self.input("input[name='paymentDescription']", "Дескрипшен")
        self.page.get_by_role("button", name="Опубликовать").click()
        self.wait_for_element("#headlessui-dialog-panel-\:r6tl\: > div")


    def press_arrow_down_and_enter(self) -> None:
        """
        Функция для имитации нажатий стрелки вниз и клавиши Enter.
        """
        self.page.keyboard.press("Enter")



       # self.click(Application.INPUT_CATEGORY)
application_coordinates = {
    "region": (500, 500),
    "category": (500, 350),
    "city": (500, 1000)
}

