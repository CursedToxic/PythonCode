weight = float(input ("Weight: "))
unit = input ("(K)g or (L)bs? ")
if unit.upper == "K":
  convert = weight/0.453592
  print ("Your weight in Lbs is: " + str(convert))
else:
  converted = weight*0.453592
  print ("Your weight in Kg is: " + str(converted))