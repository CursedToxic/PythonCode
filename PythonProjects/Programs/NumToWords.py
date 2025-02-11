phone = input("PHONE NUMBER: ")
digitMapping = {
    "0": "ZERO",
    "1": "ONE",
    "2": "TWO",
    "3": "THREE",
    "4": "FOUR",
    "5": "FIVE",
    "6": "SIX",
    "7": "SEVEN",
    "8": "EIGHT",
    "9": "NINE" 
}

output = "  "
for ch in phone:
    output += digitMapping.get(ch," !")
print(output + " ")