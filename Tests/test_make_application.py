import pytest
from pages.application_page import OpenApplicationCreatePage, OpenApplicationListPage


@pytest.mark.regression
@pytest.mark.usefixtures('user_login')
class TestCreateApplications:
    def test_create_applications(self, browser):
        for i in range(5):
            (OpenApplicationCreatePage(browser)
            .fill_application()
            .create_application()
            .check_application_result_loop(iterator=i))

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






