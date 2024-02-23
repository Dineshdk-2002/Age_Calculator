# age calculator
from datetime import datetime,time,date
def age_calculator():
  current_date = date.today()


  while True :
    birth_year = input("Enter the birth year : ")

    if birth_year.isdigit() and 1 <= int(birth_year) <= 9999:
      break
    else :
      print("Invalid input or year is invalid")

    birth_year = int(birth_year)

  while True:
    birth_month = int(input("Enter the birth month: "))
    if birth_month <= 12 :
        break
    else:
        print("Invalid input or month is invalid.")

  days_31 = [1,3,5,7,8,10,12]
  days_30 = [4,6,9,11]
  if birth_month == 2 and int(birth_year) % 4 == 0 and int(birth_year)%100 != 0 or int(birth_year)%400 == 0 :
    birth_date = int(input("Enter the date between 1-29: "))
    while birth_date > 29 or birth_date < 1:
      birth_date = int(input("Invalid input. Enter the date between 1-29: "))
  elif birth_month == 2 :
    birth_date = int(input("Enter the date between 1-28: "))
    while birth_date > 28 or birth_date < 1:
      birth_date = int(input("Invalid input. Enter the date between 1-28: "))

  elif birth_month in days_31:
    birth_date = int(input("Enter the birth date : "))
    if birth_date > 31:
      while birth_date > 31 or birth_date < 1 :
        birth_date = int(input("Invalid input Enter the date between 1-31 : "))
    else :
      birth_date = birth_date

  elif birth_month in days_30:
    birth_date = int(input("Enter the birth date : "))
    while birth_date >= 30 or birth_date < 1 :
      birth_date = int(input("Invalid input Enter the date between 1-30 : "))
    else :
      birth_date = birth_date
  if (current_date.month < birth_month) or (current_date.month == birth_month and current_date.day < birth_date):
    age = int(current_date.year) - int(birth_year ) -1
  else:
    age = int(current_date.year) - int(birth_year)

  return f"Your age is {age}"
