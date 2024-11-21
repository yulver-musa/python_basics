lenght = int(input())
depth = int(input())
hight = int(input())
perc = float(input())
mass = lenght * depth * hight
mass_litres = mass * 0.001
space = perc / 100
litres = mass_litres * (1 - space)
print(litres)
