import random

names = input("Give me everybody's name saperated by comma(,) : ")
names = names.split(", ")

# r is the length of the elements present in list names 
r = len(names)

# generating random index value for list 
random_name_choice = random.randint(0,r-1)

print(f"{names[random_name_choice]} is going to buy the meal today.")

# or we can also use {random.choice(names)} functiion which will automatically pick a random name from the list.