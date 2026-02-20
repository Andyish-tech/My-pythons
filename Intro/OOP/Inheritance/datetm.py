import datetime
from datetime import timedelta

print("\n ---- 3.2: Date and Time ----")

now = datetime.datetime.now()
print("Current date and time", now)

print("Year", now.year)
print("Weekday", now.strftime("%A"))
print("Month", now.strftime("%B"))