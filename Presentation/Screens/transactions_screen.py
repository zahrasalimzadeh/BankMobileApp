from kivy.uix.scrollview import ScrollView
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from Common.config import CARD, GREEN, RED, SUBTITLE
from Presentation.components import make_button, make_label, make_layout, make_title


class TransactionsScreen(MDScreen):
    def __init__(self, account_business_logic, **kwargs):
        super().__init__(**kwargs)
        self.account_business_logic = account_business_logic
        self.account_id = 0
        self.account_number = ""
        layout = make_layout()
        self.title = make_title("", font_style="H6", height="40dp")
        layout.add_widget(self.title)
        self.balance = make_label("", height="40dp", color=GREEN, font_style="H5")
        layout.add_widget(self.balance)
        scroll = ScrollView()
        self.transactions_box = MDBoxLayout(orientation="vertical", spacing=8, adaptive_height=True)
        scroll.add_widget(self.transactions_box)
        layout.add_widget(scroll)
        layout.add_widget(make_button("Back", self.back, color=CARD))
        self.add_widget(layout)

    def set_account(self, account_id, account_number):
        self.account_id = account_id
        self.account_number = account_number

    def on_enter(self, *args):
        self.title.text = f"Account {self.account_number}"
        self.balance.text = "..."
        self.transactions_box.clear_widgets()
        self.account_business_logic.get_balance(self.account_id, self.balance_loaded)
        self.account_business_logic.get_transactions(self.account_id, self.transactions_loaded)

    def balance_loaded(self, response):
        if response["success"]:
            self.balance.text = self.account_business_logic.format_amount(response["data"])
        else:
            self.balance.text = response["message"]

    def transactions_loaded(self, response):
        self.transactions_box.clear_widgets()

        if not response["success"]:
            self.transactions_box.add_widget(make_label(response["message"], color=RED))
            return

        for transaction in response["data"]:
            self.transactions_box.add_widget(self.make_transaction_row(transaction))

    def make_transaction_row(self, transaction):
        is_deposit = self.account_business_logic.is_deposit(transaction)
        color = GREEN if is_deposit else RED
        title = "Deposit" if is_deposit else "Withdraw"
        amount = self.account_business_logic.format_amount(transaction["amount"])
        date = self.account_business_logic.format_date(transaction["created_at"])
        row = MDCard(orientation="vertical", size_hint_y=None, height="72dp", padding=12, radius=[12], md_bg_color=CARD)
        row.add_widget(MDLabel(text=f"{title}   {amount}", theme_text_color="Custom", text_color=color))
        row.add_widget(MDLabel(text=date, theme_text_color="Custom", text_color=SUBTITLE))
        return row

    def back(self, instance):
        self.manager.current = "accounts"