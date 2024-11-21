dep_sum = float(input())
term = int(input())
percentage_flo = float(input())
percentage = percentage_flo / 100

total_sum = dep_sum + term * ((dep_sum * percentage) / 12)
print(total_sum)
