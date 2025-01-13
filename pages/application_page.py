from pages.base import Base
from Locators.application import *
from data.assertions import Assertions
from playwright.sync_api import Page


class OpenApplicationCreatePage(Base):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.open("/applications/create")
        self.iS = CreateApplication()
        self.assertion = Assertions(page)
        self.create_button = page.get_by_role(role="button", name="Опубликовать")
        self.max_count_of_applications: int = 5

    def fill_application(self):
        self.page.wait_for_timeout(500)
        self.click(self.iS.INPUT_CATEGORY)
        self.page.get_by_text("Геология").click()
        self.page.keyboard.press("Enter")
        self.input(self.iS.INPUT_SCOPE_OF_WORK, "Тест Описание работ")
        self.click_enter(self.iS.INPUT_REGION)
        self.click_enter(self.iS.INPUT_CITY)
        self.wait_for_element(self.iS.INPUT_PRICE_DETAILS)
        self.input(self.iS.INPUT_PRICE_DETAILS, "Тест Описание цены")
        return self

    def create_with_no_phone(self):
        self.create_button.click()
        self.wait_for_element(self.iS.APRUVE_NUMBER_PANEL)
        self.page.pause()
        self.click(self.iS.APRUVE_NUMBER_PANEL_CANSEL_BUTTON)
        self.route_abort(self.iS.CONFIRM_PHONE_URL)
        return self

    def create_application(self):
        self.create_button.click()
        self.assertion.check_URL("myApplications/active")
        return self

    def check_application_result_loop(self, iterator: int):
        iterator += 1
        self.assertion.check_URL("myApplications/active")
        assert self.page.locator(self.iS.LIST_OF_MY_APPLICATIONS).count() == iterator
        assert self.page.locator("span[class='f-b2']").text_content() == f"{self.max_count_of_applications - iterator}/5"
        return self



class OpenApplicationListPage(Base):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.open("/applications")
        self.iS = ListApplications()
        self.assertion = Assertions(page)
        self.contact_button = page.get_by_role("button", name="Получить контакты").first
        self.pay_now_button = page.get_by_text("Оплата сразу")
        self.pay_process_button = page.get_by_text("Оплата в процессе сделки")
        self.invoice_button = page.get_by_role("radio", name="Выставление счета")
        self.bank_card = page.get_by_role("radio", name="Банковская карта")
        self.pay_button = page.get_by_role("button", name="К оплате")
        self.continue_button = page.get_by_role("button", name="Продолжить")


    def click_first_application_commission(self):
        self.wait_for_all_elements(self.iS.LIST_OF_APPLICATIONS)
        self.page.get_by_text("за комиссию").first.click()
        self.page.wait_for_url(self.iS.APPLICATION_DETAILS_URL)
        self.click_by_locator(self.contact_button)
        return self

    def click_first_application_sales_application(self):
        self.click(self.iS.SEARCH_BUTTON)
        self.wait_for_all_elements(self.iS.LIST_OF_APPLICATIONS)
        self.click(self.iS.SEARCH_BUTTON)
        self.page.get_by_text("заявка на продажу").first.click()
        self.page.wait_for_url(self.iS.APPLICATION_DETAILS_URL)
        self.click_by_locator(self.contact_button)
        return self

    def give_me_contact_now(self):
        self.click_by_locator(self.pay_now_button)
        self.click_by_locator(self.continue_button)
        return self

    def give_me_contact_now_sales_application(self):
        self.click_by_locator(self.continue_button)
        return self

    def for_bank_card(self):
        self.click_by_locator(self.bank_card)
        self.click_by_locator(self.pay_button)
        self.page.wait_for_url(self.iS.ALFA_BANK_URL)
        self.assertion.have_text(self.iS.AMOUNT_MAJOR, "800")
        return self

    def for_payment_pdf(self):
        self.click_by_locator(self.invoice_button)
        self.click_by_locator(self.pay_button)
        self.route_abort(self.iS.PAYMENT_PDF)
        self.assertion.have_text(self.iS.PAYMENT_IS_DONE, "Счет сформирован!")
        return self



