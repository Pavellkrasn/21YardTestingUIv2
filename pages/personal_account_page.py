from playwright.sync_api import Page




class PersonalAccountPage:

    def get_personal_account_page(self, page: Page):
        return page.title()
    _TITLE_PERSONAL_ACCOUNT = "h1[class='xl:hidden text-start ']"
    _MAKE_APPLICATION_BUTTON = ""
    _ADD_COMPANY_BUTTON = ""
    _HELP_BUTTON = ""
    _MAKE_COMPANY_WRAPPER = ""

class CompanyWrapper:
    _UR_NAME_INPUT = "input[name='name']"
    _INN_INPUT = "input[name='inn']"
    _MAKE_COMPANY_BUTTON = "button[class*='179 _x']"


