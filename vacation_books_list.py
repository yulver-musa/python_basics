import math
n_pages = int(input())
pages_hour = int(input())
days = int(input())

total_time = n_pages / pages_hour
hours_per_day = total_time / days
print(math.floor(hours_per_day))
