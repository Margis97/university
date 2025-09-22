import json

import requests
from requests import Session
import curlify

from logger import MyLogger
from utils.json_utils import JsonUtils


def log_response(func):
    def wrapper(*args, **kwargs) -> requests.Response:
        response = func(*args, **kwargs)
        MyLogger().logger.info(f"Request: {curlify.to_curl(response.request)}")
        body = json.dumps(response.json(), indent=2) if JsonUtils.is_json(response.text) else response.text
        MyLogger().logger.info(f"Status code: {response.status_code}, Response: {body}")
        return response
    return wrapper

class ApiUtils:
    def __init__(self, url, headers=None):
        if headers is None:
            headers = {}
        self.session = Session()
        self.session.headers.update(headers)
        self.url = url

    def update_headers(self, headers):
        self.session.headers.update(headers)

    @log_response
    def get(self, endpoint, **kwargs):
        response = self.session.get(self.url + endpoint, **kwargs)
        return response

    @log_response
    def post(self, endpoint, data=None, json=None, **kwargs):
        response = self.session.post(self.url + endpoint, data, json, **kwargs)
        return response

    @log_response
    def delete(self, endpoint, **kwargs):
        response = self.session.delete(self.url + endpoint, **kwargs)
        return response