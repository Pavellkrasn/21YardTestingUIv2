import pytest

from pages.personal_account_page import OpenPersonalAccountPage


@pytest.mark.smoke
@pytest.mark.usefixtures('user_login')
class TestMyApplication:
    @pytest.mark.skip
    def test_delete_account(self,browser):
        OpenPersonalAccountPage(browser).delete_account()
    def test_make_company(self,browser):
        (OpenPersonalAccountPage(browser)
         .fill_company_fields()
         .create_company())