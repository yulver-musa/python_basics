n_pkt_pens = int(input())
n_pkt_mark = int(input())
l_clean = int(input())
disc = int(input())

p_pkt_pens = n_pkt_pens * 5.80
p_pkt_mark = n_pkt_mark * 7.20
p_l_clean = l_clean * 1.20
per_disc = disc / 100

total_price = p_pkt_pens + p_pkt_mark + p_l_clean
total_sum = total_price - (total_price * per_disc)
print(total_sum)
