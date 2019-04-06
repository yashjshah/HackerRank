# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

m, d, y = [int(x) for x in input().split()]
day_number = calendar.weekday(y, m, d)
day_name = calendar.day_name[day_number]
print(day_name.upper())


