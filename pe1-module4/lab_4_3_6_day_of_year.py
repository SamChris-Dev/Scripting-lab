def is_year_leap(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False

def days_in_month(year, month):
    if is_year_leap(year) == False:
        if month <= 7 and month % 2 != 0 \
        or month >= 8 and month % 2 ==0:
            return 31
        elif month == 2:
            return 28
        else:
            return 30
    elif is_year_leap(year) == True:
        if month <= 7 and month % 2 != 0 \
        or month >= 8 and month % 2 ==0:
            return 31
        elif month == 2:
            return 29
        else:
            return 30


def day_of_year(year, month, day):
    if is_year_leap(year) == False:
        return 365
    else:
        return 366

    

print(day_of_year(2000, 12, 31))
