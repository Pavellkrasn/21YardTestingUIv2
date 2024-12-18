import pytest
from pages.login_page import OpenLoginPage


@pytest.mark.smoke
class TestLogin:
    def test_user_login(self, browser):
         OpenLoginPage(browser).user_login()


