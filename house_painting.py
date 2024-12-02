x = float(input())
y = float(input())
h = float(input())

door = 1.2 * 2
window = 1.5 * 1.5

back = x * x
front = x * x - door
side_1 = x * y - window
side_2 = x * y - window
total_area_walls = back + front + side_1 + side_2
green = total_area_walls / 3.4

roof_sides = x * y + x * y
roof_fronts = 2 * (x * h/2)
total_area_roof = roof_sides + roof_fronts
red = total_area_roof / 4.3

print(f'{green:.2f}')
print(f'{red:.2f}')
