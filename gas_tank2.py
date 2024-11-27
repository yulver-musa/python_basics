gasoline_price = 2.22
diesel_price = 2.33
gas_price = 0.93

type_fuel = input().lower()
litres_fuel = float(input())
club_card = input().lower()

total_price = 0
sub_total = 0

if type_fuel == "gasoline" and club_card == "yes":
    sub_total = litres_fuel * (gasoline_price - 0.18)
elif type_fuel == "gasoline" and club_card == "no":
    sub_total = litres_fuel * gasoline_price
elif type_fuel == "diesel" and club_card == "yes":
    sub_total = litres_fuel * (diesel_price - 0.12)
elif type_fuel == "diesel" and club_card == "no":
    sub_total = litres_fuel * diesel_price
elif type_fuel == "gas" and club_card == "yes":
    sub_total = litres_fuel * (gas_price - 0.08)
elif type_fuel == "gas" and club_card == "no":
    sub_total = litres_fuel * gas_price

if 20 <= litres_fuel <= 25:
    total_price = sub_total - (sub_total * 0.08)
elif litres_fuel > 25:
    total_price = sub_total - (sub_total * 0.1)
else:
    total_price = sub_total

print(f"{total_price:.2f} lv.")
