import allure
import requests
from faker import Faker

from services.university.helpers.group_helper import GroupHelper

faker = Faker()


@allure.feature("Проверка 401 кода ошибки")
class TestGroupContract:
    def test_create_group_unauthorized(self, university_api_utils_create):
        group_helper = GroupHelper(api_utils=university_api_utils_create)
        response = group_helper.post_group(json={"name": faker.name()})

        assert response.status_code == requests.codes.forbidden, \
            (f"Wrong status_code, actual: '{response.status_code}', "
             f"expected: '{requests.codes.forbidden}'")
