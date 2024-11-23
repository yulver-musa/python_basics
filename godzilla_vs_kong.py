budget = float(input())
stunts = int(input())
costumes = float(input())

decor = budget * 0.1
if stunts > 150:
    costumes = costumes - (costumes * 0.1)
costumes_price = stunts * costumes

expenses = decor + costumes_price
diff = abs(budget - expenses)
if budget >= expenses:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")
