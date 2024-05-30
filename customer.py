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

class Bank:
    def __init__(self):
        self.customers = {}
        self.load_data()
    
    def load_data(self):
        try:
            with open('bank_data.json', 'r') as file:
                self.customers = json.load(file)
        except FileNotFoundError:
            pass
    
    def save_data(self):
        with open('bank_data.json', 'w') as file:
            json.dump(self.customers, file)
    
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

# Example usage
bank = Bank()

# Create accounts
print(bank.create_account("Alice"))
print(bank.create_account("Bob"))

# Deposit and withdraw
customer1 = bank.get_customer(12345)
print(customer1.deposit(1000))
print(customer1.withdraw(500))
print(customer1.get_balance())

# Handling non-existent account
customer2 = bank.get_customer(99999)
if customer2:
    print(customer2.get_balance())
else:
    print("Account not found.")
