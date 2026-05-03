import calendar

date = input().split()

month = int(date[0])
day = int(date[1])
year = int(date[2])

days = list(calendar.day_name)

print(days[calendar.weekday(year, month, day)].upper())