from Locators.application import ListApplications
from playwright.sync_api import TimeoutError



"""Декоратор для повторной попытки выполнения функции при возникновении ошибок,
  Ограничение на кол во попыток - 3
  Декоратор обрабатывает TimeoutError, AssertionError и перезагружает страницу или  """


def retry_on_error(func, max_retries=3):
    def wrapper(browser, *args, **kwargs):
        page = args[0]
        retries = 0
        while retries < max_retries:
            try:
                return func(browser, *args, **kwargs)
            except AssertionError as e:
                retries += 1
                print(f"{e.__class__.__name__} при выполнении {func.__name__}. Попытка {retries}/{max_retries}.")
                if retries < max_retries:
                    print("Перезагружаем страницу и пробуем снова...")
                    page.reload()  # Перезагружаем страницу
                else:
                    raise
            except TimeoutError:
                 # Извлекаем объект страницы
                page.reload()
                return
    return wrapper

"""Декоратор для клика на кнопку поиск при появлении бага с пустым листом"""

def empty_list_error(func):
    def wrapper(browser, *args, **kwargs):
        page = args[0]
        try:
            return func(browser, *args, **kwargs)
        except TimeoutError as e:
            if page.is_visible(ListApplications.IMAGE_EMPTY_ERROR, timeout=7000):
                page.click(ListApplications.SEARCH_BUTTON)
                print(f"{e.__class__.__name__} при выполнении {func.__name__}. ЛИСТ ПУСТОЙ")
                page.wait_for_selector(ListApplications.SEARCH_INPUT, timeout=12000)
            else:
                raise e
    return wrapper




