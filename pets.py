from math import floor
from math import ceil
days = int(input())
food_left = int(input())
dog_daily = float(input())
cat_daily = float(input())
tortoise_daily = float(input()) / 1000

dog_food = days * dog_daily
cat_food = days * cat_daily
tortoise_food = days * tortoise_daily

total_food = dog_food + cat_food + tortoise_food
diff = abs(total_food - food_left)

if total_food <= food_left:
    print(f"{floor(diff)} kilos of food left.")
else:
    print(f"{ceil(diff)} more kilos of food are needed.")
