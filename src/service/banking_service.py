# Banking Services
from domain.bank_account import BankAccount

class BankingService:
    bank_account = BankAccount
    def __init__(self, bank_account):
        self.bank_account = bank_account
        
    def deposit(self):
        pass
    
    def withdrawl(self):
        pass 