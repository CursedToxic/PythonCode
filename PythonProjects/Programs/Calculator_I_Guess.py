
while True:
    method = input("Please select a method: plus, minus, times or divide: ").lower()
    num1 = int(input("Please enter the first number: "))
    num2 = int(input("Please enter the second number: "))

    if method == "plus":
        print("You have chosen to add")
        print(num1 + num2)

    elif method == "minus":
        print("You have chosen to subtract")
        print(num1 - num2)

    elif method == "times":
        print("You have chosen to multiply")
        print(num1 * num2)

    elif method == "divide":
        print("You have chosen to divide")
        print(num1/num2)

    else:
        print("[ERROR]")