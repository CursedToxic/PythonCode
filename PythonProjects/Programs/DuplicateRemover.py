numbers = [1,1,2,3,5,8,13,21]
uniques = []

for number in numbers:
    if number not in uniques:
         uniques.append(number)
    print(uniques)
