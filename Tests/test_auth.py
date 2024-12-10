import pytest
from pages.login_page import Login


@pytest.mark.smoke
class TestLogin:
    def test_user_login(self, browser):
         Login(browser).user_login()


