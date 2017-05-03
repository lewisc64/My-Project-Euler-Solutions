from datetime import datetime, timedelta
import calendar
date = datetime(1901, 1, 1)
count = 0
while date < datetime(2000,12,31):
    date = date + timedelta(days = 1)
    if date.weekday() == 6 and date.day == 1:
        count += 1
print(count)
