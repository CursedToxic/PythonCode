import time

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
            if len(new_account != 6):
                raise ValueError("Account Number must be six digits.")
        else:
            raise ValueError("Account Number must be an integer.")
        
# Note: I tried the below, but haven't yet firugred it out, so I am sticking with something that lacks error handling.

# account_one = BankAccount(18052025, -204618.36, "Rob")
# account_two = BankAccount(28052025, 0.01, "Victor")

# def choose_account():
#     invalid_account_name = True

#     while invalid_account_name == True:
#         account_selection = str(input("Enter account: ")).lower()

#         if account_selection == str(account_one.owner_name).lower():
#             invalid_account_name = False

#         if account_selection == str(account_two.owner_name).lower():
#             invalid_account_name = False
    
#         else:
#             print("Enter a valid account name.")

# def how_money_moves():
#     valid_way = False
    
#     while valid_way == False:
#         move_money = str(input("Deposit or Withdraw? ")).upper()

#     if move_money != account_one.balance or account_two.balance:
#         print("Are you depositing or withdrawing?")
    
#     if move_money == "DEPOSIT" or "WITHDRAW":
#         valid_way = True

# def transfer_process_account_one():
#     valid_transfer = False      
    
#     while valid_transfer == False:
#         move_much = int(input(f"Enter Amount: "))

#         if account_one.balance <= 0:
#             print("You cannot withdraw. Please go get a job.")

#         if move_much <= account_one.balance:
#             new_balance = move_much + account_one.balance
#             time.sleep(1)
#             print(f"Your new balance is: {new_balance}")

# def transfer_process_account_two():
#     valid_transfer = False      
    
#     while valid_transfer == False:
#         move_much = int(input(f"Enter Amount: "))

#         if account_one.balance <= 0:
#             print("You cannot withdraw. Please go get a job.")

#         if move_much < account_two.balance:
#             new_balance = move_much + account_two.balance
#             time.sleep(1)
#             print(f"Your new balance is: {new_balance}")