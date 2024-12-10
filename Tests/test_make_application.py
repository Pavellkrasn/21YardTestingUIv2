import pytest
from pages.application_page import ApplicationPage

@pytest.mark.regression
@pytest.mark.usefixtures('user_login')
class TestCreateApplications:
    def test_create_applications(self, browser):
        ap = ApplicationPage(browser)
        ap.fill_application()
        ap.end_create()

