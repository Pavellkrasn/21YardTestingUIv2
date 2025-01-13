import pytest
from configuration.postgress_utils import delete_applications, update_applications_counter, get_user_id_by_email
from configuration.redis_utils import delete_cache_by_key
from data.constants import Constants
from fixtures.page import browser
from fixtures.user_company_data import create_test_data
from fixtures.user_auth import user_login
from pages.application_page import OpenApplicationCreatePage, OpenApplicationListPage
from pages.login_page import OpenLoginPage
from pages.personal_account_page import OpenPersonalAccountPage
from pages.registration_page import OpenRegistrationPage


@pytest.mark.regression
@pytest.mark.usefixtures('create_test_data')
class TestCreateApplications:
    @pytest.mark.usefixtures('user_login')
    def test_create_applications(self, browser):
        delete_applications("Тест Описание работ")
        update_applications_counter(Constants.login)
        key = get_user_id_by_email(Constants.login)
        delete_cache_by_key(key=f"user_companies:{key}")
        for i in range(5):
            (OpenApplicationCreatePage(browser)
            .fill_application()
            .create_application()
            .check_application_result_loop(iterator=i))


    def test_check_confirm_phone_frame(self,browser,create_test_data):
        (OpenRegistrationPage(browser,create_test_data)
         .fill_registration_fields()
         .click_on_checkboxes()
         .click_on_registration_button()
         .confirm_email())
        (OpenLoginPage(browser, create_test_data)
         .user_login())
        (OpenPersonalAccountPage(browser,create_test_data)
         .fill_company_fields()
         .create_company()
         .check_name_and_inn())
        (OpenApplicationCreatePage(browser)
         .fill_application()
         .create_with_no_phone())


@pytest.mark.smoke
@pytest.mark.usefixtures('user_login')
class TestResponseApplications:
    def test_load_applications_bank_card(self,browser):
        (OpenApplicationListPage(browser)
         .click_first_application_commission()
         .give_me_contact_now()
         .for_bank_card())

    def test_load_applications_screen_payment_pdf(self, browser):
        (OpenApplicationListPage(browser)
         .click_first_application_commission()
         .give_me_contact_now()
         .for_payment_pdf())

    def test_load_application_bank_card_sales_application(self,browser):
        (OpenApplicationListPage(browser)
         .click_first_application_sales_application()
         .give_me_contact_now_sales_application()
         .for_bank_card())
    def test_accredited_companies(self,browser):
        (OpenApplicationListPage(browser))
        pass


@pytest.mark.smoke
class TestApplicationsWithoutAccount:
    def test_load_applications_without_account(self,browser):
        (OpenApplicationListPage(browser)
         .click_first_application_commission()
         .give_me_contact_now())
        pass






