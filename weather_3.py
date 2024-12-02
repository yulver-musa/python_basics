degrees = float(input())
if 26.00 <= degrees <= 35.00:
    print("Hot")
elif 20.1 <= degrees < 26:
    print("Warm")
elif 15.00 <= degrees < 20.1:
    print("Mild")
elif 12.00 <= degrees < 15:
    print("Cool")
elif 5.00 <= degrees < 12:
    print("Cold")
else:
    print("unknown")
