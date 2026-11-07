from kivy.uix.widget import Widget
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField
from Common.config import CARD, RED
from Presentation.components import make_button, make_label, make_layout, make_title


class OtpScreen(MDScreen):
    def __init__(self, auth_business_logic, **kwargs):
        super().__init__(**kwargs)
        self.auth_business_logic = auth_business_logic
        layout = make_layout()
        layout.add_widget(Widget())
        layout.add_widget(make_title("Verification"))
        layout.add_widget(make_label("Enter the code sent to your phone"))
        self.code = MDTextField(hint_text="Code")
        layout.add_widget(self.code)
        self.message = make_label("", color=RED)
        layout.add_widget(self.message)
        layout.add_widget(make_button("Verify", self.verify))
        layout.add_widget(make_button("Back", self.back, color=CARD))
        layout.add_widget(Widget())
        self.add_widget(layout)

    def on_pre_enter(self, *args):
        self.code.text = ""
        self.message.text = ""

    def verify(self, instance):
        self.message.text = ""
        self.auth_business_logic.verify_otp(self.code.text.strip(), self.verify_done)

    def verify_done(self, response):
        if not response["success"]:
            self.message.text = response["message"]
            return

        self.manager.current = "accounts"

    def back(self, instance):
        self.manager.current = "login"