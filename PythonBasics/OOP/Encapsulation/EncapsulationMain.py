from BankAccount import *

account = BankAccount(18052025, -204618.36, "Rob")

print(account.get_owner_name())
print(account.get_account_number())
print(account.get_balance())

account.set_account_number(25052009)
account.set_balance(0.00)
account.set_owner_name("Victor Guo")

print(account.get_owner_name())
print(account.get_account_number())
print(account.get_balance())
print("don't get scammed")