from datetime import datetime

day_week = {
    'Monday': 52,
    'Tuesday': 52,
    'Wednesday': 52,
    'Thursday': 52,
    'Friday': 52,
    'Saturday': 52,
    'Sunday': 52,
}

n = int(input())
year = int(input())

while n != 0:
    data = input() + " " + str(year)
    data = datetime.strptime(data, "%d %B %Y")
    day_week[data.strftime("%A")] -= 1
    n -= 1

first_day = input()
day_week[first_day] += 1

if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    dec30 = datetime.strptime("30/12/" + str(year), "%d/%m/%Y")
    day_week[dec30.strftime("%A")] += 1

maax = max(day_week, key=lambda x: day_week[x])
miin = min(day_week, key=lambda x: day_week[x])
print(maax, miin)