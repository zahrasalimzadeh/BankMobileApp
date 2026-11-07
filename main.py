from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from BusinessLogic.account_business_logic import AccountBusinessLogic
from BusinessLogic.auth_business_logic import AuthBusinessLogic
from Common.config import BASE_URL
from DataAccess.api_client import ApiClient
from Presentation.Screens.accounts_screen import AccountsScreen
from Presentation.Screens.login_screen import LoginScreen
from Presentation.Screens.otp_screen import OtpScreen
from Presentation.Screens.transactions_screen import TransactionsScreen


class BankApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        api_client = ApiClient(BASE_URL)
        auth_business_logic = AuthBusinessLogic(api_client)
        account_business_logic = AccountBusinessLogic(api_client)
        manager = MDScreenManager()
        manager.add_widget(LoginScreen(auth_business_logic, name="login"))
        manager.add_widget(OtpScreen(auth_business_logic, name="otp"))
        manager.add_widget(AccountsScreen(auth_business_logic, account_business_logic, name="accounts"))
        manager.add_widget(TransactionsScreen(account_business_logic, name="transactions"))
        return manager


BankApp().run()