import pytest

from data.constants import Constants
from pages.login_page import OpenLoginPage


@pytest.fixture(scope='class')
def user_login(browser): # Статичный юзер, на котором много открытых заявок
    (OpenLoginPage(browser, create_test_data=None)
     .user_login(constants_email=Constants.login))




