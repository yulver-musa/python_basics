number_km = int(input())
part_of_day = input()

taxi_day = (number_km * 0.79) + 0.7
taxi_night = (number_km * 0.9) + 0.7
bus = number_km * 0.09
train = number_km * 0.06

if number_km >= 100:
    print(f"{train:.2f}")
elif number_km >= 20:
    print(f"{bus:.2f}")
elif number_km < 20:
    if part_of_day == "day":
        print(f"{taxi_day:.2f}")
    elif part_of_day == "night":
        print(f"{taxi_night:.2f}")
