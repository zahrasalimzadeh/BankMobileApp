import json
from kivy.network.urlrequest import UrlRequest
from Common.response import fail


class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def post(self, path, data, on_done):
        self.send(path, on_done, json.dumps(data), {"Content-Type": "application/json"})

    def get(self, path, on_done):
        self.send(path, on_done)

    def send(self, path, on_done, body=None, headers=None):
        def success(request, result):
            on_done(result)

        def failed(request, error):
            on_done(fail("Server error"))

        UrlRequest(self.base_url + path, req_body=body, req_headers=headers, on_success=success, on_failure=failed, on_error=failed)