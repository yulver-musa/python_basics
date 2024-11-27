holidays = int(input())

working_days = 365 - holidays
total_holidays = holidays * 127
total_working_days = working_days * 63
total_minutes = total_holidays + total_working_days
diff = abs(30000 - total_minutes)
yearly_hours = diff // 60
yearly_minutes = diff % 60

if total_minutes <= 30000:
    print("Tom sleeps well")
    print(f"{yearly_hours} hours and {yearly_minutes} minutes less for play")
else:
    print("Tom will run away")
    print(f"{yearly_hours} hours and {yearly_minutes} minutes more for play")
