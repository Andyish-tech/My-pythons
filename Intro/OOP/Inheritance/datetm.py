import datetime
from datetime import timedelta

print("\n ---- 3.2: Date and Time ----")

now = datetime.datetime.now()
print("Current date and time", now)

print("Year", now.year)
print("Weekday", now.strftime("%A"))
print("Month", now.strftime("%B"))

print("\n ---- 3.2: Date and Time ----")

new_year= datetime.datetime(2025, 1, 1)
print("New year:", new_year)

tomorrow =now + timedelta(days=1)
yestarday =now - timedelta(days=1)
next_week = now + timedelta(weeks=1)

print("Tomorrow: ", tomorrow.strftime("%Y-%m-%d"))
print("Yestarday:", yestarday.strftime("%Y-%m-%d"))
print("Next week:", next_week.strftime("%Y-%m-%d"))

print("\n ---- 3.2: Date and Time ----")

formatted=now.strftime('%Y-%m-%d %H:%M%S')
print("Formatted now:", formatted)

date_str= "2024-06-15 09:03:00"
parsed=datetime.datetime.strptime(date_str,"%Y-%m-%d %H:%M:%S")
print("Parsed date:", parsed)