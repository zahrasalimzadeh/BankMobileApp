from Common.response import fail


class AuthBusinessLogic:
    def __init__(self, api_client):
        self.api_client = api_client
        self.mobile = ""
        self.password = ""
        self.customer_id = 0
        self.full_name = ""

    def login(self, mobile, password, on_done):
        if not mobile or not mobile.isdigit() or len(mobile) != 11:
            on_done(fail("Invalid mobile number."))
            return

        if not password or len(password) < 6:
            on_done(fail("Invalid structure password."))
            return

        self.mobile = mobile
        self.password = password
        self.api_client.post("/api/v1/auth/login", {"mobile": mobile, "password": password}, on_done)

    def verify_otp(self, code, on_done):
        if not code or not code.isdigit() or len(code) != 5:
            on_done(fail("Invalid code."))
            return

        def verified(response):
            if response["success"]:
                self.customer_id = response["data"]["customer_id"]
                self.full_name = response["data"]["full_name"]
            on_done(response)

        self.api_client.post("/api/v1/auth/verify-otp", {"mobile": self.mobile, "password": self.password, "code": code}, verified)

    def logout(self):
        self.mobile = ""
        self.password = ""
        self.customer_id = 0
        self.full_name = ""