#select random number
import random
num = random.randint(1,10000)

#accept guess, decide if win or loss
run = True
while run:
    guess = int(input("Guess a number between 1-10000: "))
    print("|")
    if guess == int(num):
        print("Good job, you win!")
        print("|")
        run = False
    else:
        if guess >= int(num):
            print("Too high!")
            print("|")
        if guess <= int(num):
            print("Too low!")
            print("|")
        continue
    playagain = int(input("Play again? 1=yes, 2=no: "))
    if playagain == int(2):
        run = False
    else:
        run = True
