# Bank Account Class
class BankAccount:
    
    def __init__(self, db_account_number: int, owner_name: str, balance=0.00):
        self.db_account_number = db_account_number
        self.owner_name = owner_name
        self.balance = balance
        
    
    
   