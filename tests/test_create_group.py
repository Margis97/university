import allure
from faker import Faker

from services.university.models.group_request import GroupRequest
from services.university.university_service import UniversityService

faker = Faker()

@allure.feature("Проверка создания группы")
class TestCreateGroup:
    def test_create_group(self, university_api_utils_update):
        uni_service = UniversityService(api_utils=university_api_utils_update)
        group_name = faker.name()
        group_request = GroupRequest(name=group_name)
        response = uni_service.create_group(group_request)

        assert response.name == group_name, f"Wrong group name, actual: '{response.name}'"
