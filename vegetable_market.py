pr_veg = float(input())
pr_fruit = float(input())
kg_veg = int(input())
kg_fruit = int(input())

total_veg = pr_veg * kg_veg
total_fruit = pr_fruit * kg_fruit
total_sum = (total_veg + total_fruit) / 1.94
print(f'{total_sum:.2f}')
