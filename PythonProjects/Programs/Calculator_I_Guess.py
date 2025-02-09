def again():
    ask = input("Would you like to perform another operation? ").lower()
    if ask == "yes" or "yea" or "y" or "yeah" or "ye" or "yh":
        pass
    else:
        print("I'll take that as a no")


while True:
    try: 
        num1 = int(input("Please enter number1: "))
        num2 = int(input("Please enter number2: "))
        method = input("Please select a method: plus, minus, times or divide: ").lower()


        if method == "plus":
            print("You have chosen to add")
            print(int(num1) + int(num2))
            again()
            
        elif method == "minus":
            print("You have chosen to subtract")
            print(int(num1) - int(num2))
            again()

        elif method == "times":
            print("You have chosen to multiply")
            print(int(num1) * int(num2))
            again()

        elif method == "divide":
            print("You have chosen to divide")
            print(int(num1)/int(num2))
            again()

    except ValueError:
            print("[ERROR]")
