grade = float(input())

if grade >= 5.50:
    print("Excellent!")
else:
    if grade >= 4.50:
        print("Very Good")
    else:
        if grade >= 3.50:
            print("Good")
        else:
            if grade >= 3.00:
                print("Medium")
            else:
                if grade <= 3.00:
                    print("Poor")
