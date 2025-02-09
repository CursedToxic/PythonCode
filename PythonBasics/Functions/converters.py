import random

def lbs_to_kg(weight_in_lbs):
    return weight_in_lbs * 0.45

def kg_to_lbs(weight_in_kg):
    return weight_in_kg / 0.45

def respond_to_idiots(meauserment):
    choice = random.randint(1,5)
    if choice == 1:
        responses = "Please just enter K or L"
    elif choice == 2:
        responses = "Is it that hard to press [K] or [L]?"
    elif choice == 3:
        responses = "Try Again >:("
    elif choice == 4:
        responses = "..."
    elif choice == 5:
        responses = "ARE YOU STUPID JUST ENTER K OR L!!!"
    return responses

which_one = input("[K]G or [L]BS: ").upper()
measurement = str(which_one)
weight_in_kg = int(input("ENTER WEIGHT IN KG: "))
weight_in_lbs = int(input("ENTER WEIGHT IN LBS: "))

if measurement == "K":
    print(weight_in_kg)
    kg_to_lbs()
elif measurement == "L":
    print(weight_in_lbs)
    lbs_to_kg()
else:
    respond_to_idiots(measurement)