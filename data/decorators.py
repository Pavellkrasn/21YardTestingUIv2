
"""Декоратор для повторной попытки выполнения функции при возникновении ошибок,
  Ограничение на кол во попыток - 3
  Декоратор обрабатывает TimeoutError, AssertionError и перезагружает страницу или  """


def retry_on_error(func, max_retries=3):
    def wrapper(browser, *args, **kwargs):
        retries = 0
        while retries < max_retries:
            try:
                return func(browser, *args, **kwargs)
            except AssertionError as e:
                retries += 1
                print(f"{e.__class__.__name__} при выполнении {func.__name__}. Попытка {retries}/{max_retries}.")
                if retries < max_retries:
                    print("Перезагружаем страницу и пробуем снова...")
                    page = args[0]  # Извлекаем объект страницы из аргументов
                    page.reload()  # Перезагружаем страницу
                else:
                    raise
            except TimeoutError:
                page = args[0]  # Извлекаем объект страницы
                page.reload()
                return
    return wrapper



