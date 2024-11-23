holiday = float(input())
puzzle = int(input())
doll = int(input())
teddy = int(input())
minions = int(input())
truck = int(input())

pr_puzzle = 2.6
pr_doll = 3
pr_teddy = 4.1
pr_minions = 8.2
pr_truck = 2

total_toys = puzzle + doll + teddy + minions + truck

a = puzzle * pr_puzzle
b = doll * pr_doll
c = teddy * pr_teddy
d = minions * pr_minions
e = truck * pr_truck

sub1 = a + b + c + d + e

if total_toys >= 50:
    sub2 = sub1 - (sub1 * 0.25)
else:
    sub2 = sub1

total_sum = sub2 - (sub2 * 0.1)

if total_sum >= holiday:
    print(f"Yes! {(total_sum - holiday):.2f} lv left.")
else:
    print(f"Not enough money! {(holiday - total_sum):.2f} lv needed.")
