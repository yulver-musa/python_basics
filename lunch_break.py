from math import ceil
show_name = input()
ep_long = int(input())
break_time = int(input())

lunch = break_time / 8
rest = break_time / 4
left_time = break_time - lunch - rest
diff = abs(ep_long - left_time)

if ep_long <= left_time:
    print(f"You have enough time to watch {show_name} and left with {ceil(diff)} minutes free time.")
else:
    print(f"You don't have enough time to watch {show_name}, you need {ceil(diff)} more minutes.")
