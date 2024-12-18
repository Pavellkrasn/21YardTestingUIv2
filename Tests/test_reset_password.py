import pytest

from pages.reset_password_page import OpenResetPasswordPage


@pytest.mark.smoke
class TestLogin:
    def test_user_login(self, browser):
         (OpenResetPasswordPage(browser, create_test_data=None)
          .reset_password())
