#select random number
import random
num = random.randint(1,10000)

print("|--------------------------------|")
print("|       Hello and welcome        |")
print("|                                |")
print("| This is a number guessing game |")
print("|    created by Brandon Shutt    |")
print("|                                |")
print("| The game will generate a random|")
print("|  number between 1 and 10,000   |")
print("|                                |")
print("|      You can take a guess      |")
print("| and the computer will tell you |")
print("|   if you if your guess was     |")
print("|      too high or too low       |")
print("|                                |")
print("|       Have fun and enjoy!      |")
print("|--------------------------------|")
print("                                  ")

#accept guess, decide if win or loss
run = True
while run:
    guess = int(input("Guess a number between 1-10000: "))
    print("|")
    if guess == int(num):
        print("              Good job, you win!                ")
        print("                                  .''.          ")     
        print("      .''.      .        *''*    :_\/_:     .   ")
        print("    :_\ /_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'.")
        print(" .''.: /\ :   ./)\   ':'* /\ * :  '..'.  -=:o:=-")
        print(":_\/_:'.:::.    ' *''*    * '.\'/.' _\(/_'.':'.'")
        print(": /\ : :::::     *_\/_*     -= o =-  /)\    '  *")
        print(" '..'  ':::'     * /\ *     .'/.\'.   '         ")
        print("     *            *..*         :                ")
        print("            *                                   ")
        print("       *                                        ")
        run = False
    else:
        if guess >= int(num):
            print("↓Your guess was too high!↓")
            print("|------------------------|")
        if guess <= int(num):
            print("↑Your guess was too low!↑")
            print("|-----------------------|")
        continue
    playagain = int(input("Play again? 1=yes, 2=no: "))
    if playagain == int(2):
        run = False
    else:
        run = True
