# new_list = [new_item for item in list]

# using numered lists
numbers = [1, 2, 3, 4, 5]
new_list = [n+1 for n in numbers]
print(new_list)

# using characters and strings
name = "Satyam"
changed_name = [letter for letter in name]
print(changed_name)

# using range to loop
ranges = range(1, 5)
doubled_range = [n*2 for n in ranges]
print(doubled_range)
