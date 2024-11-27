fuel_type = input().lower()
fuel_litres = float(input())

if (fuel_type == "gasoline" or fuel_type == "diesel" or fuel_type == "gas") and fuel_litres >= 25:
    print(f"You have enough {fuel_type}.")
elif (fuel_type == "gasoline" or fuel_type == "diesel" or fuel_type == "gas") and fuel_litres < 25:
    print(f"Fill your tank with {fuel_type}!")
elif fuel_type != "gasoline" or fuel_type != "diesel" or fuel_type != "gas":
    print("Invalid fuel!")
