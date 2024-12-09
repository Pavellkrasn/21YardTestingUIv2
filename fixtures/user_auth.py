import pytest
from pages.login_page import Login


@pytest.fixture(scope='class')
def user_login(browser):
    m = Login(browser)
    m.user_login()