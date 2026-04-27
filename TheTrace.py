import openpyxl
from openpyxl import Workbook
from datetime import datetime
import os

file_name = "Geek_log.xlsx"

#Geek Log(In excel structure)

if os.path.exists(file_name):
 workbook = openpyxl.load_workbook(file_name)
 sheet = workbook.active

else:
 workbook = Workbook()
 sheet = workbook.active 
 sheet.title = "Nates Black Book Geek Log"
 sheet.append(["Type", "Grams", "Date", "Time"])

print("Welcome Nate lets log the session\n")


#Loop 1 TYPE

while True:
 print("What are you geeking on? (Blunt, Bongrip ,Bowl, Geeb, Shrooms.")
 smoke_type = input("Enter choice: ").lower()


 if smoke_type in ["blunt","bongrip", "bowl", "geeb", "shrooms"]:
    break
 else:
  print("Invalid input pls try again fn! \n")

  
#Loop 2 Grams

while True:
 grams = input("How many grams are you ingesting yn?")

 try:
     grams = float(grams)
     break
 except:
     print("Enter a valid number. \n")


#Loop 3 Date and Time

while True:
 date_input = input("Punch in  date (MM/DD/YYYY):  ")
 time_input = input("Punch in  time (HH:MM AM/PM): ")

 try:
    datetime.striptime(date_input + " " + time_input, "%m/%d/%Y %I:%M %p")
    break
 except:
    print("Invalid date/time properly format fn! \n")


#Saves to Geek Log


sheet.append ([smoke_type, grams, date_input, time_input])
workbook.save(file_name)

print("\nSuccessful save burger.")
print("Happy geeks.")
















