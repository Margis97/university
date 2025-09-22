import requests

from services.general.helpers.base_helper import BaseHelper


class UserHelper(BaseHelper):
    ME = "/users/me/"

    def get_me(self) -> requests.Response:
        response = self.api_utils.get(self.ME)
        return response
