budget = float(input())
graphic_card = int(input())
cpu = int(input())
ram = int(input())

sum_graph = graphic_card * 250
price_cpu = sum_graph * 0.35
sum_cpu = cpu * price_cpu
price_ram = sum_graph * 0.1
sum_ram = price_ram * ram

total_sum = sum_graph + sum_cpu + sum_ram
if graphic_card > cpu:
    total_sum = total_sum - (total_sum * 0.15)

diff = abs(budget - total_sum)

if total_sum <= budget:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")
