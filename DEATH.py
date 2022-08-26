import sys
import time
import requests
from bs4 import BeautifulSoup
import random

#functions for cool typing effect
def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.02)
  
def typingInput(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.02)
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

#ask user for name, birthday and gender
name = typingInput("Tell me your name: ")
year = typingInput("What is your birth year?: ")
monthinput = typingInput("What month were you born in?: ")
user_day = int(typingInput("What day were you born on?: "))
genderinput = typingInput("Are you male or female?: ")

#sort what user typed as birth month
JAN = ["Jan", "jan", "january", "January"]
FEB = ["February", "february", "Feb", "feb"]
MAR = ["March", "march", "Mar", "mar"]
APR = ["April", "april", "Apr", "apr"]
MAY = ["May", "may"]
JUN = ["June", "june", "Jun", "jun"]
JUL = ["July", "july", "Jul", "jul"]
AUG = ["August", "august", "Aug", "aug"]
SEP = ["September", "september", "Sept", "sept", "Sep", "sep"]
OCT = ["October", "october", "Oct", "oct"]
NOV = ["November", "november", "Nov", "nov"]
DEC = ["December", "december", "Dec", "dec"]

#turn birth month into a digit
if any(keyword in monthinput for keyword in JAN):
    month = ("01")
elif any(keyword in monthinput for keyword in FEB):
    month = ("02")
elif any(keyword in monthinput for keyword in MAR):
    month = ("03")
elif any(keyword in monthinput for keyword in APR):
    month = ("04")
elif any(keyword in monthinput for keyword in MAY):
    month = ("05")
elif any(keyword in monthinput for keyword in JUN):
    month = ("06")
elif any(keyword in monthinput for keyword in JUL):
    month = ("07")
elif any(keyword in monthinput for keyword in AUG):
    month = ("08")
elif any(keyword in monthinput for keyword in SEP):
    month = ("09")
elif any(keyword in monthinput for keyword in OCT):
    month = ("10")
elif any(keyword in monthinput for keyword in NOV):
    month = ("11")
elif any(keyword in monthinput for keyword in DEC):
    month = ("12")

#turn what user typed as day, turn it into digit
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
    
#take genderinput and turn it into number
MAN = "M", "m", "B", "b", "D", "d", "G", "g"
WOMAN = "W", "w", "F", "f", "G", "g", "Gurl"
if any(keyword in genderinput for keyword in MAN):
    gender = 76
if any(keyword in genderinput for keyword in WOMAN):
    gender = 81

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
bar = "[======================================]"
print(loading)
for c in bar:
    time.sleep(0.3)
    sys.stdout.write(c)
    sys.stdout.flush()

#estimate time of death and show results
print("\n   _                   _")
print(" _( )                 ( )_")
print("(_, |      __ __      | ,_)")
print("   \\'\    /  ^   \    /'/")
print("    '\\'\,/\       \,/'/'")
print("      '\\| []   [] |/'")
print("        (_  /^\  _)")
print("          \  ~  /")
print("          /XXXXX\\")
print("        /'/{^^^}\'\\")
print("    _,/'/'  ^^^  '\'\,_")
print("   (_, |           | ,_)")
print("     (_)           (_)")
print("------------------------------------------")

#pick death year
Deathlist = int(year) + int(gender) + random.randint(1, 3)
Deathyear = (str(Deathlist))

#pick random month
Monthlist = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
Deathmonth = random.choice(Monthlist)

#pick random day
Daylist = ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th", "12th", "13th", "14th", "15th", "16th", "17th", "18th", "19th", "20th", "21st", "22nd", "23rd", "24th", "25th", "26th", "27th", "28th", "29th", "30th"]
Deathday = random.choice(Daylist)

#pick random time of day
random_hour = random.randint(1, 12)
random_minute = random.randint(1, 59)
am_pm = ["am", "pm"]
random_ampm = random.choice(am_pm)
Deathtime = (f"{random_hour}:{random_minute}{random_ampm}")

print(name + ", it seems that your fate is sealed.")
print(f"Your life will end at {Deathtime}, on {Deathmonth} {Deathday} {Deathyear}.")
print("------------------------------------------")
print("Enjoy the time you have left, have a nice day!")
