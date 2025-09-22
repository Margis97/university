from services.auth.helpers.authorization_helper import AuthorizationHelper
from services.auth.helpers.user_helper import UserHelper
from services.auth.models.login_request import LoginRequest
from services.auth.models.login_response import LoginResponse
from services.auth.models.register_request import RegisterRequest
from services.auth.models.register_response import RegisterResponse
from utils.api_utils import ApiUtils


class AuthService:
    SERVICE_URL = "http://127.0.0.1:8000"

    def __init__(self, api_utils: ApiUtils):
        self.api_utils = api_utils
        self.authorization_helper = AuthorizationHelper(self.api_utils)
        self.user_helper = UserHelper(self.api_utils)

    def register(self, register_request: RegisterRequest) -> RegisterResponse:
        response = self.authorization_helper.post_register(data=register_request.model_dump())
        return RegisterResponse(**response.json())

    def login(self, login_request: LoginRequest) -> LoginResponse:
        response = self.authorization_helper.post_login(data=login_request.model_dump())
        return LoginResponse(**response.json())