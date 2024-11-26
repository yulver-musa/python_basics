from math import pi
geo_figures = input()
area = 0

if geo_figures == "square":
    a = float(input())
    area = a * a
    print(f'{area:.3f}')
elif geo_figures == "rectangle":
    a = float(input())
    b = float(input())
    area = a * b
    print(f'{area:.3f}')
elif geo_figures == "circle":
    r = float(input())
    area = pi * r * r
    print(f'{area:.3f}')
elif geo_figures == "triangle":
    a = float(input())
    h = float(input())
    area = 0.5 * a * h
    print(f'{area:.3f}')
