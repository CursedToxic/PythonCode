while True:
    try:
        year = int(input("ENTER A YEAR: "))
        if year % 4 == 0 and not year % 100 == 0:
            print("IT IS A LEAP YEAR")

        else:
            print("THIS IS NOT A LEAP YEAR")
            print("TRY ANOTHER YEAR")
    
    except ValueError:
        print("INVALID")