from BankAccount import *
import time

account_one = BankAccount(18052025, -204618.36, "Rob")
account_two = BankAccount(28052025, 0.01, "Victor")

invalid_account_name = True

while invalid_account_name == True:
    account_selection = str(input("Enter account: ")).lower()

    # if account_selection != account_one.owner_name.lower() or account_two.owner_name.lower():
    #     print("INVALID ACCOUNT.")
    #     again = str(input("Enter Another Account?[(Y)es/(N)o]: "))

    #     if again.lower() == 'y' or 'yes':
    #         print("Okay, let's try again...")
    #     else:
    #         invalid_account_name = False
    #         break
    
    if account_selection == str(account_one.owner_name).lower():
        invalid_account_name = False
        move_money = str(input("Deposit or Withdraw? ")).upper()

        # if move_money != account_one.balance or account_two.balance:
        #     print("Are you depositing or withdrawing?")

        if move_money == "DEPOSIT":
            move_much = int(input(f"Enter Amount to {move_money}: "))
            new_balance = move_much + account_one.balance
            time.sleep(1)
            print(f"Your new balance is: {new_balance}")

        elif move_money == "WITHDRAW":
            if account_one.balance <= 0:
                print("You cannot withdraw. Please go get a job.")

            elif account_one.balance > 0:
                move_much = int(input(f"Enter Amount to {move_money}: "))
                if move_much > account_one.balance:
                    print(f"Cannot Withdraw. Please enter an amount less than {account_one.balance}.")
                
    elif account_selection == str(account_two.owner_name).lower():
        invalid_account_name = False
        move_money = str(input("Deposit or Withdraw? ")).lower()

        if move_money == "deposit":
            move_much = int(input(f"Enter Amount to {move_money}: "))
            new_balance = move_much + account_two.balance
            time.sleep(1)
            print(f"Your new balance is: {new_balance}")

        elif move_money == "withdraw":
            if account_two.balance <= 0:
                print("You cannot withdraw. Please go get a job.")

            elif account_two.balance > 0:
                move_much = int(input(f"Enter Amount to {move_money}: "))
                if move_much > account_two.balance:
                    print(f"Cannot Withdraw. Please enter an amount less than {account_two.balance}.")