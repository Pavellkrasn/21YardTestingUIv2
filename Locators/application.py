
import re

class CreateApplication:
    INPUT_CATEGORY = "input[placeholder='Например: монолитные работы']"
    INPUT_SCOPE_OF_WORK = "input[placeholder='Введите описание объема работ ']"
    INPUT_REGION = "input[placeholder='Укажите регион']"
    INPUT_CITY = "input[placeholder='Укажите город']"
    INPUT_PRICE_DETAILS = "input[placeholder='Например: не более 1000р за кв.м.']"
    APRUVE_NUMBER_PANEL = "div[id*='headlessui-dialog-panel']"
    APRUVE_NUMBER_PANEL_CANSEL_BUTTON = "div[id *= 'headlessui-dialog-panel'] > button"

    LIST_OF_MY_APPLICATIONS = "//*[@id='page-content']/div/div/div"


class ListApplications:
    LIST_OF_APPLICATIONS = "a[href*='/applications/details']"
    AMOUNT_MAJOR = "span[class='amount__major']"
    ALFA_BANK_URL = re.compile(r"https://alfa\.rbsuat\.com/.*")
    PAYMENT_PDF = re.compile(r".*/api/marketplace/applications/generate_pdf_invoice/\d+.*")
    PAYMENT_IS_DONE = "//h2[text()='Счет сформирован!']"
    APPLICATION_DETAILS_URL = re.compile(r"https://dev\.21yard\.com/applications/details.*")
    SEARCH_BUTTON = "button[class*='12 b']"










