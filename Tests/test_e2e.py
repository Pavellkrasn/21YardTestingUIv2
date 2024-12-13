import pytest

from Tests.test_auth import TestLogin
from Tests.test_make_application import TestCreateApplications
from Tests.test_personal_account import TestMyApplication
from Tests.test_registration import TestRegistration
from fixtures.page import browser
from pages.personal_account_page import OpenPersonalAccountPage


@pytest.mark.smoke
class TestE2E:
    def test_e2e(self, browser):
        TestRegistration.test_user_registration(browser=browser)
        TestLogin.test_user_login(browser)
        TestMyApplication.test_make_company(browser=browser)
        '''
        toDo: 
        - втсавка в бд
        - отклик на заявку с процентом
        - добавить мониторинг 
        - добавить чекер 
        - вставить аллюр
        '''
        for i in [1,2,3,4,5] :
            TestCreateApplications.test_create_applications(browser=browser)
        TestMyApplication.test_delete_account(browser=browser)




