import pytest
from pages.login_page import Login


@pytest.fixture(scope='class')
def user_login(browser):
    Login(browser).user_login()

