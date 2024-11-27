from math import floor
from math import ceil

magnolias = 3.25
hyacinth = 4
roses = 3.5
cactus = 8

n_magnolias = int(input())
n_hyacinth = int(input())
n_roses = int(input())
n_cactus = int(input())
gift_price = float(input())

a = magnolias * n_magnolias
b = hyacinth * n_hyacinth
c = roses * n_roses
d = cactus * n_cactus
total_sell = a + b + c + d
tax = total_sell * 0.05
profit = total_sell - tax
diff = abs(gift_price - profit)

if profit >= gift_price:
    print(f"She is left with {floor(diff)} leva.")
else:
    print(f"She will have to borrow {ceil(diff)} leva.")
