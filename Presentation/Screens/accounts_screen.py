from kivy.uix.scrollview import ScrollView
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from Common.config import CARD, RED, SUBTITLE
from Presentation.components import make_button, make_label, make_layout, make_title


class AccountsScreen(MDScreen):
    def __init__(self, auth_business_logic, account_business_logic, **kwargs):
        super().__init__(**kwargs)
        self.auth_business_logic = auth_business_logic
        self.account_business_logic = account_business_logic
        layout = make_layout()
        self.welcome = make_title("", font_style="H5")
        layout.add_widget(self.welcome)
        layout.add_widget(make_label("Your accounts"))
        scroll = ScrollView()
        self.accounts_box = MDBoxLayout(orientation="vertical", spacing=12, adaptive_height=True)
        scroll.add_widget(self.accounts_box)
        layout.add_widget(scroll)
        layout.add_widget(make_button("Logout", self.logout, color=CARD))
        self.add_widget(layout)

    def on_enter(self, *args):
        self.welcome.text = f"Welcome {self.auth_business_logic.full_name}"
        self.accounts_box.clear_widgets()
        self.account_business_logic.get_accounts(self.auth_business_logic.customer_id, self.accounts_loaded)

    def accounts_loaded(self, response):
        self.accounts_box.clear_widgets()

        if not response["success"]:
            self.accounts_box.add_widget(make_label(response["message"], color=RED))
            return

        for account in response["data"]:
            self.accounts_box.add_widget(self.make_account_card(account))

    def make_account_card(self, account):
        card = MDCard(
            orientation="vertical",
            size_hint_y=None,
            height="90dp",
            padding=16,
            radius=[14],
            md_bg_color=CARD,
            ripple_behavior=True,
            on_release=self.account_clicked
        )
        card.account = account
        card.add_widget(MDLabel(text=f"Account {account['account_number']}", font_style="H6"))
        card.add_widget(MDLabel(text=f"Opened {account['opening_date'][:10]}", theme_text_color="Custom", text_color=SUBTITLE))
        return card

    def account_clicked(self, card):
        account = card.account
        self.manager.get_screen("transactions").set_account(account["id"], account["account_number"])
        self.manager.current = "transactions"

    def logout(self, instance):
        self.auth_business_logic.logout()
        self.manager.get_screen("login").password.text = ""
        self.manager.current = "login"