points = int(input())

bonus_points_l_100 = 5
bonus_points_btw = points * 0.2
bonus_points_m_1000 = points * 0.1

if points <= 100:
    if points % 2 == 0:
        print(bonus_points_l_100 + 1)
        print(points + bonus_points_l_100 + 1)
    elif points % 5 == 0:
        print(bonus_points_l_100 + 2)
        print(points + bonus_points_l_100 + 2)
    else:
        print(bonus_points_l_100)
        print(points + bonus_points_l_100)
elif 100 < points < 1000:
    if points % 2 == 0:
        print(bonus_points_btw + 1)
        print(points + bonus_points_btw + 1)
    elif points % 5 == 0:
        print(bonus_points_btw + 2)
        print(points + bonus_points_btw + 2)
    else:
        print(bonus_points_btw)
        print(points + bonus_points_btw)
elif points > 1000:
    if points % 2 == 0:
        print(bonus_points_m_1000 + 1)
        print(points + bonus_points_m_1000 + 1)
    elif points % 5 == 0:
        print(bonus_points_m_1000 + 2)
        print(points + bonus_points_m_1000 + 2)
    else:
        print(bonus_points_m_1000)
        print(points + bonus_points_m_1000)
