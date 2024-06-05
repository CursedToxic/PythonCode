while True:
    try:
        year = int(input("ENTER A YEAR: "))
        if year % 4 == 0 and not year % 100 == 0:
            print("IT IS A LEAP YEAR")
            break

        elif year < 0:
            print("INVALID YEAR, MUST NOT BE NEGATIVE")
            break

        else:
            print("THIS IS NOT A LEAP YEAR")
            break
    
    except ValueError:
        print("INVALID")