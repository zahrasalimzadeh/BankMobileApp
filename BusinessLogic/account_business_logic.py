from Common.response import fail


class AccountBusinessLogic:
    def __init__(self, api_client):
        self.api_client = api_client

    def get_accounts(self, customer_id, on_done):
        if not customer_id:
            on_done(fail("Invalid customer."))
            return

        self.api_client.get(f"/api/v1/accounts?customer_id={customer_id}", on_done)

    def get_balance(self, account_id, on_done):
        if not account_id:
            on_done(fail("Invalid account."))
            return

        self.api_client.get(f"/api/v1/accounts/{account_id}/balance", on_done)

    def get_transactions(self, account_id, on_done):
        if not account_id:
            on_done(fail("Invalid account."))
            return

        self.api_client.get(f"/api/v1/transactions?account_id={account_id}", on_done)

    def format_amount(self, amount):
        return f"{amount:,.0f}"

    def format_date(self, text):
        return text[:16].replace("T", " ")

    def is_deposit(self, transaction):
        return transaction["transaction_type"] == 1