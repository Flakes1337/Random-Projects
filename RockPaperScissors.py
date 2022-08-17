#welcome screen
print("|--------------------------------|")
print("|       Hello and welcome        |")
print("|                                |")
print("|  This is Rock Paper Scissors   |")
print("|    created by Brandon Shutt    |")
print("|                                |")
print("|   **  I hope you enjoy!!  **   |")
print("|--------------------------------|")
print("                                  ")

#computer picks random move
import random
computermove = random.randint(1,3)

#player picks move
run = True
while run:
        print("----------")
        playermove = int(input(" 1=ROCK\n 2=PAPER\n 3=SCISSORS \n Type 1,2 or 3 to select: "))
        print(" |")
        if playermove == 1:
            print("YOU SELECTED ROCK!\n |")
        if computermove == 1:
            print("COMPUTER SELECTED ROCK\n |")
        if playermove == 2:
            print("YOU SELECTED PAPER\n |")
        if computermove == 2:
            print("COMPUTER SELECTED PAPER\n |")
        if playermove == 3:
            print("YOU SELECTED SCISSORS\n |")
        if computermove == 3:
            print("COMPUTER SELECTED SCISSORS\n |")
        if playermove >= 4:
            print("INVALID MOVE\n |")
        if playermove == computermove:
            print("ITS A TIE\n |")
            
        elif playermove == 1:
            if computermove == 3:
                print("ROCK SMASHES SCISSORS\n | YOU WIN!!")
            else:
                print("PAPER COVERS ROCK\n | YOU LOSE!\n |")
             
        elif playermove == 2:
            if computermove == 1:
                print("PAPER COVERS ROCK\n | YOU WIN!!\n |")
            else:
                print("SCISSORS CUTS PAPER\n | YOU LOSE!\n |")
             
        elif playermove == 3:
            if computermove == 2:
                print("SCISSORS CUTS PAPER\n | YOU WIN!!\n")
            else:
                print("PAPER COVERS ROCK\n | YOU LOSE!\n |")
        print("----------")     
        playagain = int(input("Play again? 1=yes, 2=no: "))
        if playagain == int(2):
            run = False
        else:
            run = True
