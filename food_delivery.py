m_chicken = int(input())
m_fish = int(input())
m_veg = int(input())

pr_m_c = m_chicken * 10.35
pr_m_f = m_fish * 12.4
pr_m_v = m_veg * 8.15
pr_del = 2.5
sub_total = pr_m_c + pr_m_f + pr_m_v
pr_des = sub_total * 0.2
total_sum = sub_total + pr_des + pr_del
print(f"{total_sum:.2f}")
