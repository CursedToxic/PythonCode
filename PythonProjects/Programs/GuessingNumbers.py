import random

secretNumber = random.randint(0,10)
guessCount = 0
guessLimit = 3
while guessCount < guessLimit:
    guess = int(input ("GUESS: "))
    guessCount += 1
    if guess == secretNumber:
        print("YOU WIN")
        break
else:
    print("YOU FAILED")
    print(f"THE ANSWER WAS {secretNumber}")
