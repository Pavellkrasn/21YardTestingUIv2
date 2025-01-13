

from data.decorators import retry_on_error, empty_list_error
from fixtures.page import browser
from fixtures.user_company_data import create_test_data
from pages.application_page import OpenApplicationCreatePage, OpenApplicationListPage
from pages.login_page import OpenLoginPage
from pages.personal_account_page import OpenPersonalAccountPage
from pages.registration_page import OpenRegistrationPage

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
        self._create_company(browser, create_test_data)

        # 4. Создание 5ти заявок
        self._create_application(browser)

        # 5. Проверка заявки с комиссией
        self._check_application_with_commission_bank_card(browser)

        # 6. Проверка заявки с оплатой сейчас через платежку
        self._check_application_with_commission_payment_pdf(browser)

        # 7. Проверка заявки с оплатой сейчас через карту
        self._check_application_sales_application_bank_card(browser)

        # 8. удаляем аккаунт
        self.delete_user(browser,create_test_data)

    def _register_user(self, browser, create_test_data):
        please = OpenRegistrationPage(browser, create_test_data)
        please.fill_registration_fields()
        please.click_on_checkboxes()
        please.click_on_registration_button()
        please.confirm_email()
        please.confirm_phone()
        please.reset_password()

    @retry_on_error
    def _login_user(self, browser, create_test_data):
        please = OpenLoginPage(browser, create_test_data)
        please.user_login()

    def _create_company(self, browser,create_test_data):
        please = OpenPersonalAccountPage(browser,create_test_data)
        please.fill_company_fields()
        please.create_company()
        please.check_name_and_inn()

    @retry_on_error
    def _create_application(self, browser):
        please = OpenApplicationCreatePage(browser)
        please.fill_application()
        please.create_application()

    @empty_list_error
    def _check_application_with_commission_payment_pdf(self, browser):
        please = OpenApplicationListPage(browser)
        please.click_first_application_commission()
        please.give_me_contact_now()
        please.for_payment_pdf()

    @empty_list_error
    def _check_application_with_commission_bank_card(self, browser):
        please = OpenApplicationListPage(browser)
        please.click_first_application_commission()
        please.give_me_contact_now()
        please.for_bank_card()

    @empty_list_error
    def _check_application_sales_application_bank_card(self, browser):
        please = OpenApplicationListPage(browser)
        please.click_first_application_sales_application()
        please.give_me_contact_now_sales_application()
        please.for_bank_card()

    @retry_on_error
    def delete_user(self, browser,create_test_data):
        page = OpenPersonalAccountPage(browser,create_test_data)
        page.delete_account()




'''
toDo: 
- добавить чекер 
'''



