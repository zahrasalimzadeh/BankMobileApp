import json
from kivy.network.urlrequest import UrlRequest
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField


class BankApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        layout = MDBoxLayout(orientation="vertical", padding=30, spacing=20,
                             md_bg_color=(0.133, 0.133, 0.133, 1))
        layout.add_widget(Widget())
        layout.add_widget(Image(source="images/bank.png", size_hint_y=None, height="96dp"))
        layout.add_widget(MDLabel(text="Bank", halign="center", font_style="H4",
                                  size_hint_y=None, height="48dp"))
        layout.add_widget(MDLabel(text="Sign in to your account", halign="center",
                                  size_hint_y=None, height="30dp",
                                  theme_text_color="Custom",
                                  text_color=(0.6, 0.7, 0.8, 1)))
        self.mobile = MDTextField(hint_text="Mobile")
        layout.add_widget(self.mobile)
        self.password = MDTextField(hint_text="Password", password=True)
        layout.add_widget(self.password)
        button = MDCard(size_hint_y=None, height="56dp", radius=[14],
                        md_bg_color=(0.216, 0.353, 0.498, 1),
                        ripple_behavior=True, on_release=self.login)
        button.add_widget(MDLabel(text="Login", halign="center"))
        layout.add_widget(button)
        layout.add_widget(Widget())
        return layout

    def login(self, instance):
        body = json.dumps({"mobile": self.mobile.text, "password": self.password.text})
        UrlRequest(
            "http://127.0.0.1:8001/api/v1/auth/login",
            req_body=body,
            req_headers={"Content-Type": "application/json"},
            on_success=self.login_success,
            on_failure=self.login_failed,
            on_error=self.login_failed,
        )

    def login_success(self, request, result):
        print(result["message"])

    def login_failed(self, request, error):
        print("Server error")


BankApp().run()