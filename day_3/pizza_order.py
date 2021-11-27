print("Welcome to the Python pizza Deliveries.")

size = input("What size of pizza do you want? s,m,l : ")
price = 0

if size=="s":
    price = 15
    print("You have selected small size pizza.")
elif size=="m":
    price = 20
    print("You have selected medium size pizza.")
elif size=="l":
    price = 25
    print("You have selected large size pizza.")
else:
    print("You have entered wrong value, please select s,m or l.")

want_pepperoni = input("Do you want peperroni? y or n : ")

if want_pepperoni=="y":
    if size=="s":
        price += 2
    else:
        price += 3

want_cheese = input("Do you want extra cheese? y or n : ")

if want_cheese=="y":
    price += 1

print(f"Your total bill is : {price}")
