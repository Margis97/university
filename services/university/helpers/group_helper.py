import requests

from services.general.helpers.base_helper import BaseHelper


class GroupHelper(BaseHelper):
    GROUPS = "/groups/"

    def post_group(self, json: dict) -> requests.Response:
        response = self.api_utils.post(self.GROUPS, json=json)
        return response

    def get_group(self, group_id: int) -> requests.Response:
        group_id_str = str(group_id)
        endpoint = self.GROUPS + group_id_str
        response = self.api_utils.get(endpoint)
        return response

    def delete_group(self, group_id: int) -> requests.Response:
        group_id_str = str(group_id)
        endpoint = self.GROUPS + group_id_str
        response = self.api_utils.delete(endpoint)
        return response
