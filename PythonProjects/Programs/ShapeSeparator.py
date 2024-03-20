print("I AM A SHAPE GUESSER. I WILL GUESS YOUR SHAPE USING QUESTIONS.")

q1 = input("Q1: Does your shape have a rounded side? ").upper()
if q1 == "YES":
    q2a = input("Q2: Does your shape look elongated? ").upper()
    if q2a == "YES":
        print("Your shape is an oval.")
    else:
        q2a2 = input("Q3: Does your shape have rounded corners? ").upper()
        if q2a2 == "YES":
            print("Your shape is a squircle.")
        else:
            print("Your shape is a circle.")
elif q1 == "NO":
    q2b = input("Q2: Does your shape have more than 4 sides? ").upper()
    if q2b == "YES":
        q2b1 = input("Q3: Does your shape have more than 6 sides? ").upper()
        if q2b1 == "YES":
            q2b1a = input("Q4: Does your shape have more than 8 sides? ").upper()
            if q2b1a == "YES":
                q2b1a1 = input("Q5: Does your shape have more than 10 sides? ").upper()
                if q2b1a1 == "YES":
                    q2b1a1a = input("Q6: Does your shape have more than 12 sides? ").upper()
                    if q2b1a1a == "YES":
                        numsides = int(input("How many sides does your shape have?"))
                        print(f"Your shape is a {numsides}-gon")
                    else:
                        q2b1a1a2 = input("Q7: Does your shape have more than 11 sides? ").upper()
                        if q2b1a1a2 == "YES":
                            print("Your shape is a dodecagon.")
                        else:
                            print("Your shape is a hendecagon.")
                else:
                    q2b1a1b = input("Q6: Does your shape have more than 9 sides? ").upper()
                    if q2b1a1b == "YES":
                        print("Your shape is a decagon.")
                    else:
                      print("Your shape is a nonagon.")
            else:
                q2b1a2 = input("Q5: Does your shape have more than 7 sides? ").upper()
                if q2b1a2 == "YES":
                    print("Your shape is an octagon.")
                else:
                    print("Your shape is a septagon.")
        else:
            q2b1b = input("Q4: Does your shape have more than 5 sides? ").upper()
            if q2b1b == "YES":
                print("Your shape is a hexagon.")
            else:
                print("Your shape is a pentagon.")
    else:
        q2b2 = input("Q3: Does your shape have more than 3 sides? ").upper()
        if q2b2 == "YES":
            q2b2a = input("Q4: Does your shape have even sides? ").upper()
            if q2b2a == "YES":
                q2b2a3 = input("Q5: Does your shape have even angles? ").upper()
                if q2b2a3 == "YES":
                    print("Your shape is a square.")
                else:
                    print("Your shape is a rhombus.")
            else:
                q2b2a3 = input("Q5: Does your shape have even angles? ").upper()
                if q2b2a3 == "YES":
                    print("Your shape is a rectangle.")
                else:
                    print("Your shape is a parallelogram.")
        else:
            print("Your shape is a triangle.")