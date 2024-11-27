number_v = int(input())
number_p1 = int(input())
number_p2 = int(input())
number_h = float(input())

total_p1 = number_p1 * number_h
total_p2 = number_p2 * number_h
total_litres = total_p1 + total_p2

percentage_fullness = (total_litres / number_v) * 100
percentage_p1 = (total_p1 / total_litres) * 100
percentage_p2 = (total_p2 / total_litres) * 100
overflow = total_litres - number_v

if number_v >= total_litres:
    print(f"The pool is {percentage_fullness:.2f}% full. Pipe 1: {percentage_p1:.2f}%. Pipe 2: {percentage_p2:.2f}%.")
else:
    print(f"For {number_h} hours the pool overflows with {overflow:.2f} liters.")
