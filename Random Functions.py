
# Function that adds a time "Typing" effect to print and input commands
import time,sys
 
def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  
def typingInput(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.100)
  value = input()  
  return value
  
typingPrint("Oh??           Thats not good...")