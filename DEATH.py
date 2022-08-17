import sys
import time

#Functions for typing effect
def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  
def typingInput(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  value = input()  
  return value

#Welcome screen
print("        .'''''.        ..||..'''''''...")
print("       / ##### \       : ||            ''.")
print("      | ## # ## |      :.||...''''''....  '.")
print("      | #  #  # |        ||             ''''")
print("      | ####### |     .  ||")
print("       \ ##### /     /| < _>")
print("        \ ### /     / |/< _>")
print("      ..''   ''... /  | < _>")
print("    .'            /   | /||             Hello, fool.")
print("    '                 |/ ||        I am the grim reaper.")
print("    |   |     '..     |  ||")
print("    |   |     |  '...''  ||     Today I will be determining")
print("    |  |       |         ||        THE DAY YOU WILL DIE.")
print("     \ |       |         ||")
print("     |\|       |         || Just answer a few simple questions.")
print("     \|         |        ||             if you dare.")
print("      |         |        ||")
print("      |         |        ||")
print("     |           |       ||")
print("   __|           |__     ||")
print("  /   '.........'   \    ||")
print("   ''''''     ''''''     ##")
print("---------------------------------------------------------------")

#questions
name = typingInput("What is thy name?: ")
birthyear = typingInput("Now tell me your birth year: ")
birthmonth = typingInput("Now your birth month: ")
birthday = typingInput("Tell me the day you were born: ")
print("------------------------------------")

#Repeating results
print("Ah, so your name is " + name + " and you were born on the " + birthday + " of " + birthmonth + " in the year " + birthyear + "...")
print("\nHow interesting...")
print("------------------------------------")

#fake loading bar
loading= "CALCULATING TIME OF DEATH... Please hold...\n"
bar = "[=============================]"
print(loading)
for c in bar:
    time.sleep(0.5)
    sys.stdout.write(c)
    sys.stdout.flush()
    
#ask the poor sap if they really want to know
run = True
while run:
    typingPrint("\nOh? \nThat cant be right.... \nSucks to be you lol.\n")
    question = int(input("Are you sure you want to know?\n1=Yes\n2=No\n-----\nYes or No?: "))
        
        if question == int(1):
        continue
        
    else run = False
   

#Results
print("   _                   _")
print(" _( )                 ( )_")
print("(_, |      __ __      | ,_)")
print("   \'\    /  ^   \    /'/")
print("    '\'\,/\       \,/'/'")
print("      '\| []   [] |/'")
print("        (_  /^\  _)")
print("          \  ~  /")
print("          /XXXXX\\")
print("        /'/{^^^}\'\\")
print("    _,/'/'  ^^^  '\'\,_")
print("   (_, |           | ,_)")
print("     (_)           (_)")
print("-----------------------------")
