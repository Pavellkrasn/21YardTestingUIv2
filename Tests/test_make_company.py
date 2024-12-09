import pytest
from pages.login_page import Login


@pytest.mark.regression
@pytest.mark.usefixtures('user_login')
class TestMakeCompany:
    def test_make_company(self, browser):
        m = Login(browser)
        m.user_login()
                                                    