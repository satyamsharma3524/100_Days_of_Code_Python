heights = input("Enter the height of the peoples saperating them by a space : ").split()
total_height = 0
length_of_array = 0

# creating a for loop to add total elements in array without using sum() function and counting the elements in array without using len() function 
for height in heights:
    total_height = total_height + int(height)
    length_of_array += 1

print(f"Total height is : {total_height}")
print(f"Number of person is : {length_of_array}")
average_height = round(total_height / length_of_array)
print(f"{average_height} is your average height.")