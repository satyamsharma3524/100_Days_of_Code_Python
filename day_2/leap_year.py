year = int(input("Enter the year you want to check : "))

if year%4==0:
    if year%100==0:
        if year%400==0:
            print("This is a leap year.")
        else:
            pass
    else:
        print("This is a leap year.")
else:
    print("This is not a leap year.")