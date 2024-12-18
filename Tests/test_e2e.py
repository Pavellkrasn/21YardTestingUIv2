from playwright.async_api import Playwright

from data.decorators import retry_on_error
from fixtures.page import browser
from fixtures.user_company_data import create_test_data
from pages.application_page import OpenApplicationCreatePage, OpenApplicationListPage
from pages.login_page import OpenLoginPage
from pages.personal_account_page import OpenPersonalAccountPage
from pages.registration_page import OpenRegistrationPage
from playwright._impl._errors import TimeoutError

import pytest


@pytest.mark.e2e
@pytest.mark.usefixtures('create_test_data')
class TestE2E:

    def test_e2e(self, browser, create_test_data):
        # 1. Регистрация
        self._register_user(browser, create_test_data)

        # 2. Авторизация
        self._login_user(browser, create_test_data)

        # 3. Создание компании
        self._create_company(browser)

        # 4. Создание 5ти заявок
        self._create_application(browser)

        # 5. Проверка заявки с комиссией
        self._check_application_with_commission_bank_card(browser)

        # 6. Проверка заявки с оплатой сейчас через платежку
        self._check_application_with_commission_payment_pdf(browser)

        # 7. Проверка заявки с оплатой сейчас через карту
        self._check_application_sales_application_bank_card(browser)

        # 8. удаляем аккаунт
        self.delete_user(browser)

    @retry_on_error
    def _register_user(self, browser, create_test_data):
        please = OpenRegistrationPage(browser, create_test_data)
        please.fill_registration_fields(create_test_data)
        please.click_on_checkboxes()
        please.click_on_registration_button()

    @retry_on_error
    def _login_user(self, browser, create_test_data):
        please = OpenLoginPage(browser, create_test_data)
        please.user_login(create_test_data)  # Используйте проверки для успешной авторизации
        please.page.screenshot()

    @retry_on_error
    def _create_company(self, browser):
        please = OpenPersonalAccountPage(browser)
        please.fill_company_fields()
        please.create_company()

    @retry_on_error
    def _create_application(self, browser):
        please = OpenApplicationCreatePage(browser)
        please.fill_application()
        please.create_application()


    @retry_on_error
    def _check_application_with_commission_payment_pdf(self, browser):
        please = OpenApplicationListPage(browser)
        please.click_first_application_commission()
        please.give_me_contact_now()
        please.for_payment_pdf()

    @retry_on_error
    def _check_application_with_commission_bank_card(self, browser):
        please = OpenApplicationListPage(browser)
        please.click_first_application_commission()
        please.give_me_contact_now()
        please.for_bank_card()

    @retry_on_error
    def _check_application_sales_application_bank_card(self, browser):
        please = OpenApplicationListPage(browser)
        please.click_first_application_sales_application()
        please.give_me_contact_now_sales_application()
        please.for_bank_card()

    @retry_on_error
    def delete_user(self, browser):
        page = OpenPersonalAccountPage(browser)
        page.delete_account()




'''
toDo: 
- добавить чекер 
- Проверка номера (дропнуть запрос на цифры в тг)
- Восстановление пароля (проверка запроса на бэк) 
'''



