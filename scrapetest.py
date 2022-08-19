#imports
import requests
from bs4 import BeautifulSoup
import sys
import random

url = "https://happyhappybirthday.net/en/1996/06/07"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

#generic input for year
year = (1996)

#parse for fun facts
week_day = soup.find("div", class_="col-md-4 col-sm-4 text-center wochentag")
weekday = week_day.find("p")
yearsold = soup.find("div", class_="years-old")
monthsold = soup.find("h3", class_="bg-green")
weeksold = soup.find("h3", class_="bg-lblue")
daysold = soup.find("h3", class_="bg-red")
zodiac_sign = soup.find("div", class_="col-md-4 col-sm-4 text-center sternzeichen")
zodiacsign = zodiac_sign.find("h3")

#you share birthdays with these people
shared_birthday1 = soup.find("div", class_="col-sm-6")
#shared_birthday2 = shared_birthday1.find_all("h5")
#shared_birthday2 = shared_birthday1.find_all("div", class_="birthday link")
#shared_birthday3 = shared_birthday2.find_all("img", class_="img-thumbnail")

#print fun fact results
print(weekday.text)
print("----------------\nYou have been alive for:")
print(yearsold.text.strip() + " years.") 
print(monthsold.text + ".")
print(weeksold.text + ".")
print(daysold.text + ".")
print("Your zodiac sign is, " + zodiacsign.text + ".")

#print(shared_birthday1.text)

#ask user what month they were born, then sort what they typed
monthinput = ("June") #input("What month were you born in?: ")
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

#convert what user typed into birth month into a digit
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

genderinput = input("Are you male or female?: ")      

MAN = "M", "m", "B", "b", "D", "d", "G", "g"
WOMAN = "W", "w", "F", "f", "G", "g", "Gurl"
if any(keyword in genderinput for keyword in MAN):
    gender = ("76")
if any(keyword in genderinput for keyword in WOMAN):
    gender = ("81")


Monthlist = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
Deathmonth = random.choice(Monthlist)
print(Deathmonth)
