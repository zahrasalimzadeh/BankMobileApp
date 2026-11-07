from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField
from Common.config import RED
from Presentation.components import make_button, make_label, make_layout, make_title


class LoginScreen(MDScreen):
    def __init__(self, auth_business_logic, **kwargs):
        super().__init__(**kwargs)
        self.auth_business_logic = auth_business_logic
        layout = make_layout()
        layout.add_widget(Widget())
        layout.add_widget(Image(source="images/bank.png", size_hint_y=None, height="96dp"))
        layout.add_widget(make_title("Bank"))
        layout.add_widget(make_label("Sign in to your account"))
        self.mobile = MDTextField(hint_text="Mobile")
        layout.add_widget(self.mobile)
        self.password = MDTextField(hint_text="Password", password=True)
        layout.add_widget(self.password)
        self.message = make_label("", color=RED)
        layout.add_widget(self.message)
        layout.add_widget(make_button("Login", self.login))
        layout.add_widget(Widget())
        self.add_widget(layout)

    def login(self, instance):
        self.message.text = ""
        self.auth_business_logic.login(self.mobile.text.strip(), self.password.text, self.login_done)

    def login_done(self, response):
        if not response["success"]:
            self.message.text = response["message"]
            return

        self.manager.current = "otp"