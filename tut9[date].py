from datetime import datetime
from datetime import date

today=date.today()


def age(year,month,day):
    year=today.year-year
    month=today.month-month
    if month<today.month:
        month=month+12
        year=year-1
    day=today.day-day
    return year,month,day
print(age(1996,10,14))
