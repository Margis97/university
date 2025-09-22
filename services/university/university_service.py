from services.general.models.base_response import BaseResponse
from services.university.helpers.group_helper import GroupHelper
from services.university.helpers.student_helper import StudentHelper
from services.university.models.group_request import GroupRequest
from services.university.models.group_response import GroupResponse
from services.university.models.student_request import StudentRequest
from services.university.models.student_response import StudentResponse
from utils.api_utils import ApiUtils


class UniversityService:
    SERVICE_URL = "http://127.0.0.1:8001"

    def __init__(self, api_utils: ApiUtils):
        self.api_utils = api_utils
        self.group_helper = GroupHelper(self.api_utils)
        self.student_helper = StudentHelper(self.api_utils)

    def create_group(self, group_request: GroupRequest) -> GroupResponse:
        response = self.group_helper.post_group(json=group_request.model_dump())
        return GroupResponse(**response.json())

    def create_student(self, student_request: StudentRequest) -> StudentResponse:
        response = self.student_helper.post_student(json=student_request.model_dump())
        return StudentResponse(**response.json())

    def get_group(self, group_id: int) -> GroupResponse:
        response = self.group_helper.get_group(group_id=group_id)
        return GroupResponse(**response.json())

    def delete_group(self, group_id: int) -> BaseResponse:
        response = self.group_helper.delete_group(group_id=group_id)
        return BaseResponse(**response.json())

