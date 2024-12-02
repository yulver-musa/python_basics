h = float(input())
w = float(input())
h_cm = h * 100
w_cm = w * 100
w_cm_a = w_cm - 100
w_cm_total = w_cm_a // 70
h_cm_total = h_cm // 120
total = (w_cm_total * h_cm_total) - 3
print(f'{total:.0f}')
