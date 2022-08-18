#imports
import requests
from bs4 import BeautifulSoup
import sys

gender = ("Female")

url = "https://happyhappybirthday.net/en/1996/06/07"
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

print("----------------")
print("you share birthdays with:")
#print(shared_birthday1.text)

if gender == ("Male") or ("male"):
    maledeath = 76 - int(yearsold.text.strip())
    print(maledeath)
    print("male")
if gender == ("Female") or ("female"):
    femaledeath = 81 - int(yearsold.text.strip())
    print(femaledeath)
    print("female")