#imports
import requests
from bs4 import BeautifulSoup
import sys

#ask user for birthday and translate for program

year = input("What is your birth year?: ")

user_month = input("What is your birth month?: ")
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

user_day = int(input("What day were you born on?: "))
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

url = "https://happyhappybirthday.net/en/" + year + "/" + month + "/" + day + ""
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

#parse for fun facts
daysold = soup.find("h3", class_="bg-red")
weeksold = soup.find("h3", class_="bg-lblue")
monthsold = soup.find("h3", class_="bg-green")
week_day = soup.find("div", class_="col-md-4 col-sm-4 text-center wochentag")
weekday = week_day.find("p")
hours_old = soup.find("div", class_="zahlen text-center")
hoursold = hours_old.find("span", class_="number-count minuten")

#print fun fact results
print(weekday.text)
print("| You have been alive for |")
print(monthsold.text)
print(weeksold.text)
print(daysold.text)
print(hoursold.text)