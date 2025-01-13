class PersonalAccount:
    TITLE_PERSONAL_ACCOUNT = "h1[class='xl:hidden text-start ']"
    ADD_COMPANY_BUTTON = "//*[@id='page-content']/div/div/div[2]/button"
    MAKE_COMPANY_WRAPPER = ""

    WRAPPER_LOCATOR = "div[class*='isOpen']"
    WRAPPER_INPUT_COMPANY_NAME = "input[placeholder='ООО/ОАО/ИП']"
    WRAPPER_INPUT_COMPANY_INN = "input[name='inn']"
    WRAPPER_BUTTON_CREATE_COMPANY = "//div[text()='Создать компанию']"

    DELETE_ACCOUNT_BUTTON = "//button[text()='Удалить аккаунт']"
    ACTUALY_DELETE = "//div[text()='Удалить']"
    EXIT_ACCOUNT_BUTTON = "//button[text()='Выход']"
    SETTINGS_BUTTON = "(//span[text()='Настройки'])[1]"

    MY_COMPANIES_BUTTON = "(//span[text()='Мои компании'])[1]"
    MY_COMPANY = "div[class='flex flex-col gap-4 flex-1']"
    MY_COMPANY_NAME_TITLE = "(//h3)[1]"
    MY_COMPANY_INN_TITLE = "//div/span[contains(text(), 'ИНН:')]"

    MY_PROFILE_BUTTON = "(//span[text()='Мой профиль'])[1]"
    SAVE_DATA_BUTTON = "//div[text()='Сохранить данные']"
    INPUT_MIDDLE_NAME = "input[name='middleName']"
    INPUT_LAST_NAME = "input[name='lastName']"


class CompanyWrapper:
    UR_NAME_INPUT = "input[name='name']"
    INN_INPUT = "input[name='inn']"
    MAKE_COMPANY_BUTTON = "button[class*='179 _x']"
