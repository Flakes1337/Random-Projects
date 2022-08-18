#imports
import sys
import time
import requests
from bs4 import BeautifulSoup


#functions for cool typing effect
def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.04)
  
def typingInput(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.04)
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


#ask user for birthday and translate for program

name = typingInput("Tell me your name: ")

year = typingInput("What is your birth year?: ")

user_month = typingInput("What is your birth month?: ")
if user_month == ("January"):
    month = ("01")
elif user_month == ("january"):
    month = ("01")
elif user_month == ("February"):
    month = ("02")
elif user_month == ("february"):
    month = ("02")
elif user_month == ("March"):
    month = ("03")
elif user_month == ("march"):
    month = ("03")
elif user_month == ("April"):
    month = ("04")
elif user_month == ("april"):
    month = ("04")
elif user_month == ("May"):
    month = ("05")
elif user_month == ("may"):
    month = ("05")
elif user_month == ("June"):
    month = ("06")
elif user_month == ("june"):
    month = ("06")
elif user_month == ("July"):
    month = ("07")
elif user_month == ("july"):
    month = ("07")
elif user_month == ("August"):
    month = ("08")
elif user_month == ("august"):
    month = ("08")
elif user_month == ("September"):
    month = ("09")
elif user_month == ("september"):
    month = ("09")
elif user_month == ("October"):
    month = ("10")
elif user_month == ("october"):
    month = ("10")
elif user_month == ("November"):
    month = ("11")
elif user_month == ("november"):
    month = ("11")    
elif user_month == ("December"):
    month = ("12")
elif user_month == ("december"):
    month = ("12")

user_day = int(typingInput("What day were you born on?: "))
if user_day <= 10:
    if user_day == 1:
        day = ("01")
    if user_day == 2:
        day = ("02")
    if user_day == 3:
        day = ("03")
    if user_day == 4:
        day = ("04")
    if user_day == 5:
        day = ("05")
    if user_day == 6:
        day = ("06")
    if user_day == 7:
        day = ("07")
    if user_day == 8:
        day = ("08")
    if user_day == 9:
        day = ("09")
if user_day >= 10:
    day = (str(user_day))

gender = typingInput("Are you male or female?: ")


#webscrape data

url = "https://happyhappybirthday.net/en/" + year + "/" + month + "/" + day + ""
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")


#parse for fun facts

week_day = soup.find("div", class_="col-md-4 col-sm-4 text-center wochentag")
weekday = week_day.find("p")

yearsold = soup.find("div", class_="years-old")

monthsold = soup.find("h3", class_="bg-green")

weeksold = soup.find("h3", class_="bg-lblue")

daysold = soup.find("h3", class_="bg-red")

zodiac_sign = soup.find("div", class_="col-md-4 col-sm-4 text-center sternzeichen")
zodiacsign = zodiac_sign.find("h3")

#shared_birthday1 = soup.find("div", class_="col-sm-6")


#print fun facts

print("-----------------------------")
typingPrint(weekday.text + "\n")
typingPrint("You have been alive for:\n")
typingPrint(yearsold.text.strip() + " years.\n")
typingPrint(monthsold.text + "\n")
typingPrint(weeksold.text + "\n")
typingPrint(daysold.text + "\n")
typingPrint("Your zodiac sign is, " + zodiacsign.text + "\n")
print("-----------------------------")
#print("you share birthdays with:")
#print(shared_birthday1.text)


#fake loading bar

loading= "CALCULATING TIME OF DEATH... Please hold...\n"
bar = "[===========================================]"
print(loading)
for c in bar:
    time.sleep(0.5)
    sys.stdout.write(c)
    sys.stdout.flush()


#death results

print("\n   _                   _")
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

if gender == ("Male") or ("male"):
    76 - int(yearsold.text.strip()) = int(maledeath)
    print(maledeath)