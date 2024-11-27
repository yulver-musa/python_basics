from math import floor
from math import ceil
area_vineyard = int(input())
grape_per_sq_m = float(input())
litres_needed = int(input())
workers = int(input())

total_grape = area_vineyard * grape_per_sq_m
wine = (total_grape * 0.4) / 2.5
diff = abs(wine - litres_needed)
per_worker = diff / workers

if wine >= litres_needed:
    print(f"Good harvest this year! Total wine: {floor(wine)} liters.")
    print(f"{ceil(diff)} liters left -> {ceil(per_worker)} liters per person.")
else:
    print(f"It will be a tough winter! More {floor(diff)} liters wine needed.")
