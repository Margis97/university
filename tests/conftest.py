import time

import pytest
import requests
from faker import Faker

from services.auth.auth_service import AuthService
from services.auth.models.login_request import LoginRequest
from services.auth.models.register_request import RegisterRequest
from services.university.models.group_request import GroupRequest
from services.university.university_service import UniversityService
from utils.api_utils import ApiUtils

faker = Faker()


@pytest.fixture(scope="session", autouse=True)
def auth_service_readiness():
    timeout = 180
    start_time = time.time()
    while time.time() < start_time + timeout:
        try:
            response = requests.get(AuthService.SERVICE_URL + "/docs")
            response.raise_for_status()
        except:
            time.sleep(1)
        else:
            break
    else:
        raise RuntimeError(f"Auth service doesn't started during '{timeout}' sec")


@pytest.fixture(scope="function", autouse=False)
def auth_api_utils_create():
    api_utils = ApiUtils(url=AuthService.SERVICE_URL)
    return api_utils


@pytest.fixture(scope="function", autouse=False)
def university_api_utils_create():
    api_utils = ApiUtils(url=UniversityService.SERVICE_URL)
    return api_utils


@pytest.fixture(scope="function", autouse=False)
def access_token(auth_api_utils_create):
    auth_service = AuthService(auth_api_utils_create)
    username = faker.user_name()
    password = "aZ!12333" + faker.word()

    auth_service.register(RegisterRequest(
        username=username,
        password=password,
        password_repeat=password,
        email=faker.email()
    ))

    response = auth_service.login(LoginRequest(username=username, password=password))
    return response.access_token


@pytest.fixture(scope="function", autouse=False)
def auth_api_utils_update(auth_api_utils_create, access_token):
    auth_api_utils_create.update_headers({"Authorization": "Bearer " + access_token})


@pytest.fixture(scope="function", autouse=False)
def university_api_utils_update(university_api_utils_create, access_token):
    api_utils = university_api_utils_create
    api_utils.update_headers({"Authorization": "Bearer " + access_token})
    return api_utils


@pytest.fixture(scope="function", autouse=False)
def create_group(university_api_utils_update):
    api_utils = university_api_utils_update
    uni_service = UniversityService(api_utils=api_utils)
    group_name = faker.name()
    group_request = GroupRequest(name=group_name)
    response = uni_service.create_group(group_request)
    return response, uni_service
