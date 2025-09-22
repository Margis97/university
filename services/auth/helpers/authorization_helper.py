import requests

from services.general.helpers.base_helper import BaseHelper


class AuthorizationHelper(BaseHelper):
    REGISTER = "/auth/register/"
    LOGIN = "/auth/login/"


    def post_register(self, data: dict) -> requests.Response:
        response = self.api_utils.post(self.REGISTER, data=data)
        return response

    def post_login(self, data: dict) -> requests.Response:
        response = self.api_utils.post(self.LOGIN, data=data)
        return response
