'''
Author:Sebastian Lopez-Gallardo
Date:1/29/2025
Description:Program that simulates bank in order to practice OPP in python
'''

class Bank:
    title = ""
    
    #Constructor
    def __init__(self, title, customer_name, current_balance, minimum_balance):     
        self.title = title
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance

    #Check if the entered value is valid if so adds it otherwise it return error message adn continues working
    def deposit(self, amount):
        try:
            amount = float(amount)
            self.current_balance += amount
            return "Succesfully deposited $" + str(amount)
        except ValueError:
            return "Enter valid number!"
    
    #Check if the entered value is valid if so adds it otherwise it return error message adn continues working
    def withdraw(self, amount):
        try:
            amount = float(amount)
            if (amount <= 0):
                return "Enter valid number!"
            
            if ((self.current_balance-amount) < self.minimum_balance):
                return "Remaining balance cannot be less than " + str(self.minimum_balance)
        
            self.current_balance -= amount
            return "Succesfully withdrawn $" + str(amount) + "\nRemaining balance: $" + str(self.current_balance)
        except ValueError:
            return "Enter valid number!"


    #Displays bank object as string
    def __str__(self):
        total = "Bank: %s\nCustomer's Name: %s\nCurrent balance:%s\n" % (self.title, self.customer_name, self.current_balance)
        return total
    

class SavingAccount(Bank):

    def __init__(self, title, customer_name, current_balance, minimum_balance, account_number, routing_number, interest_rate):
        super().__init__(title, customer_name, current_balance, minimum_balance)
        self.account_number = account_number
        self.routing_number = routing_number
        self.interest_rate = interest_rate

class CheckingAccount(Bank):

    def __init__(self, title, customer_name, current_balance, minimum_balance, account_number, routing_number, transfer_limit):
        super().__init__(title, customer_name, current_balance, minimum_balance)
        self.account_number = account_number
        self.routing_number = routing_number
        self.transfer_limit = transfer_limit


    

b1 = Bank("Truist", "Jose", 10, 1)

b2 = Bank("Chase", "John", 100, 10)

#testing
print(b1.deposit("j"))
print(b1.deposit(50000))
print(b1.deposit("j"))
print(b1.deposit(50))
print(b1.deposit("j"))
print(b1.withdraw(50))
print(b1.deposit("j"))
print(b1.withdraw("-9050000"))
print(b1.withdraw("j"))
print(b1.withdraw(50))
print(b1.withdraw(-50000))

print(b1)


