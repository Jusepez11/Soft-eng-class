import Bank

class SavingAccount(Bank.Bank):

    def __init__(self, title, customer_name, current_balance, minimum_balance, account_number, routing_number, interest_rate):
        super().__init__(title, customer_name, current_balance, minimum_balance)
        self.account_number = account_number
        self.routing_number = routing_number
        self.interest_rate = interest_rate