import pytest
from pages.application_page import ApplicationPage

@pytest.mark.regression
@pytest.mark.usefixtures('user_login')
class TestCreateApplications:
    def test_create_applications(self, browser):
        (ApplicationPage(browser)
         .fill_application()
         .create_with_no_phone())


