from dotenv import load_dotenv


load_dotenv()# Это нужно, чтобы переменные окружения (такие как логины, пароли, api tokens) не хранились в коде, а подгружались из файла .env. Это актуально только для локальных прогонов; для запуска через CI переменные будут храниться и подтягиваться из git-secrets.


pytest_plugins = [
    'fixtures.page',
    'fixtures.user_auth',
    'fixtures.user_company_data'
]