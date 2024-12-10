import random
from typing import Dict, Optional
from faker import Faker


class RegistrationDataBuilder:

    def __init__(self, faker: Faker = None):
        self.fake = faker or Faker()
        self.data: Dict[str, Optional[str]] = {
            "email": None,
            "password": "test_password",
            "phone": None,
            "name": None
        }

    def generate_phone(self) -> str:
        return "+79"+"".join(random.choices("0123456789", k=9)) # Генерация уникального телефона

    def generate_email(self) -> str:
        return self.fake.email()  # Генерация уникального эмейла

    def generate_name(self) -> str:
        return self.fake.first_name()  # Генерация имени

    def build(self) -> Dict[str, str]:
        self.data["email"] = self.generate_email()
        self.data["phone"] = self.generate_phone()
        self.data["name"] = self.generate_name()
        return self.data

class CreateCompanyBuilder:
    def __init__(self):
        self.data: Dict[str, Optional[str]]={
            "company_name": None,
            "inn":None
        }
    def generate_company_name(self) -> str:
        pass

    def generate_inn(self)->str:
        pass

    def build(self) ->Dict[str,str]:
        self.data["company_name"] = self.generate_company_name()
        self.data["inn"] = self.generate_inn()
        return self.data

