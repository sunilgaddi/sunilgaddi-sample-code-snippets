import random
import json

class Customer:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposit of {amount} successful. Current balance: {self.balance}"
        else:
            raise ValueError("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                return f"Withdrawal of {amount} successful. Current balance: {self.balance}"
            else:
                return "Insufficient funds."
        else:
            raise ValueError("Withdrawal amount must be positive.")
    
    def get_balance(self):
        return f"Current balance: {self.balance}"
    
    def to_dict(self):
        return {
            "name": self.name,
            "account_number": self.account_number,
            "balance": self.balance
        }

class Bank:
    def __init__(self):
        self.customers = {}
        self.load_data()
    
    def load_data(self):
        try:
            with open('/Users/sunil/Desktop/Collection/test_cases/bank_data.json', 'r') as file:
                data = json.load(file)
                for account_number, customer_data in data.items():
                    self.customers[int(account_number)] = Customer(**customer_data)
        except FileNotFoundError:
            pass
    
    def save_data(self):
        with open('/Users/sunil/Desktop/Collection/test_cases/bank_data.json', 'w') as file:
            json.dump({str(account_number): customer.to_dict() if isinstance(customer, Customer) else customer for account_number, customer in self.customers.items()}, file)
    
    def create_account(self, name):
        account_number = random.randint(10000, 99999)
        while account_number in self.customers:
            account_number = random.randint(10000, 99999)
        self.customers[account_number] = Customer(name, account_number)
        self.save_data()
        return f"Account created successfully. Account number: {account_number}"
    
    def get_customer(self, account_number):
        if account_number in self.customers:
            return self.customers[account_number]
        else:
            return None
