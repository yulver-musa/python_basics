speed = float(input())

if speed <= 10:
    print("slow")
else:
    if speed > 10:
        print("average")
    else:
        if speed > 50:
            print("fast")
        else:
            if speed > 150:
                print("ultra fast")
            else:
                if speed > 1000:
                    print("extremely fast")
