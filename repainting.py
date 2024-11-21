plastic = int(input())
paint = int(input())
water = int(input())
hours = int(input())
paint_per = paint / 10

pr_a = (plastic + 2) * 1.5
pr_b = (paint + paint_per) * 14.5
pr_c = water * 5
pr_d = 0.4
total_pr = pr_a + pr_b + pr_c + pr_d
pr_e = (total_pr * 0.3) * hours
total_sum = total_pr + pr_e
print(total_sum)
