class BankAccount:
    def __init__(self, account_number, balance, owner_name):
        self.account_number = account_number
        self.balance = balance
        self.owner_name = owner_name

    def get_account_number(self):
        return self.account_number
    
    def get_balance(self):
        return self.balance

    def get_owner_name(self):
        return self.owner_name
    
    def set_owner_name(self, new_name):
        if isinstance(new_name, str):
            self.owner_name = new_name
        else:
            raise ValueError("Name must be a string.")
    
    def set_balance(self, new_balance):
        if isinstance(new_balance, float):
            self.balance = new_balance
        else:
            raise ValueError("Balance must be float.")
        
    def set_account_number(self, new_account):
        if isinstance(new_account, int):
            self.account_number = new_account
        else:
            raise ValueError("Account Number must be an integer.")
