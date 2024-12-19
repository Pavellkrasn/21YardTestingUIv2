import re


class ResetPassword:
    INPUT_RESET_PASSWORD = "input[placeholder='Укажите E-mail, указанный при регистрации']"
    BUTTON_RESET = "//div[text()='Восстановить пароль']"
    RESET_PASSWORD_URL = re.compile(r"^https://dev\.21yard\.com/api/marketplace/auth/users/forget-password/")

