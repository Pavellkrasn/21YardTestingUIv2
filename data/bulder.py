import random
from typing import Dict, Optional
from faker import Faker
import string


class RegistrationDataBuilder:

    def __init__(self):
        self.fake = Faker("ru_RU") # Генерация данных под русскую локализацию
        self.data: Dict[str, Optional[str]] = {
            "email": None,
            "password": "test_password",
            "phone": None,
            "name": None
        }

    def generate_phone(self) -> str:
        return "+79"+"".join(random.choices("0123456789", k=9)) # Генерация уникального телефона

    def generate_email(self) -> str:
        return self.fake.email()  # Генерация уникальной почты

    def generate_name(self) -> str:
        return self.fake.first_name()  # Генерация имени

    def build(self) -> Dict[str, str]:
        self.data["email"] = self.generate_email()
        self.data["phone"] = self.generate_phone()
        self.data["name"] = self.generate_name()
        return self.data

class CreateCompanyBuilder:
    def __init__(self):
        self.fake = Faker('ru_RU')
        self.data: Dict[str, Optional[str]]={
            "company_name": None,
            "inn":None
        }
    def generate_company_name(self) -> str:
        prefix = random.choice(["ИП","ОАО","ООО"])
        if prefix == "ИП":
            return f"ИП {self.fake.name()}"
        else:
            return f"{prefix} Название компании №{random.randint(1000,9999)}"


    def generate_inn(self)->str:
        return "".join(random.choices(string.digits, k=12)) # ИНН максимум 12 символов

    def build(self) ->Dict[str,str]:
        self.data["company_name"] = self.generate_company_name()
        self.data["inn"] = self.generate_inn()
        return self.data

