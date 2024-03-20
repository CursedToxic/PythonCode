numbers =  [5,2,5,2,2]
#Change numbers to print different letters
for item in numbers:
    print('x'* item)

print("-------------")#OR
    
for item in numbers:
    output = ''
    for count in range(item):
        output += 'x'
    print(output)