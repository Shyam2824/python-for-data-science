# create calender

import calendar
year= eval(input("Enter the year: "))
Months= eval(input("Enter the Months: "))

cal= calendar.month(year, Months)

print(cal)
