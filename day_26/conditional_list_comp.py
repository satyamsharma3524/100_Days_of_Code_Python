# new_list = [new_item for item in list if test_condition]

names = ["satyam", "shivam", "ram", "garry", "roshni", "kajal", "simran", "simar"]

short_names = [name for name in names if len(name) <= 5]
upper_names = [name.upper() for name in names if len(name) > 5]

print(short_names)
print(upper_names)
