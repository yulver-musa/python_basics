mackerel_pr = float(input())
sprinkle_pr = float(input())
bonito = float(input())
scad = float(input())
mussels = float(input())

sub_bonito = mackerel_pr + mackerel_pr * 0.6
total_bonito = bonito * sub_bonito

sub_scad = sprinkle_pr + sprinkle_pr * 0.8
total_scad = scad * sub_scad

total_mussels = mussels * 7.50

total = total_bonito + total_scad + total_mussels

print(f'{total:.2f}')
