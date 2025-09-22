import requests

from services.general.helpers.base_helper import BaseHelper


class StudentHelper(BaseHelper):
    STUDENTS = "/students/"

    def post_student(self, json: dict) -> requests.Response:
        response = self.api_utils.post(self.STUDENTS, json=json)
        return response