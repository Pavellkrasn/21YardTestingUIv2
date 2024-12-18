import pytest

from data.bulder import CompanyDataBuilder, UserDataBuilder


@pytest.fixture(scope='class')
def create_test_data():
    user_data = UserDataBuilder().build()
    company_data = CompanyDataBuilder().build()
    return {
        'email': user_data['email'],
        'phone': user_data['phone'],
        'name': user_data['name'],
        'password': user_data['password'],
        'company_name': company_data['company_name'],
        'inn': company_data['inn']
    }

