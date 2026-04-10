def is_year_leap(year):
    if year % 4 == 0 and year % 100 != 0 :
        return True
    elif year % 400 == 0:
            return True
    else:
         return False

user_year = int(input("Enter your year:"))


if is_year_leap(user_year):
     print("Hooray! The year is a leap year")
else:
     print("Oops! Year entered is not a leap year")