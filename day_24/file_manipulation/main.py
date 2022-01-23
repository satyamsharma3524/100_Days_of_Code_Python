# file = open("my_file.txt")
# content = file.read()
# print(content)
# file.close()

# opening file using with keyword
with open("my_file.txt") as file:
    content = file.read()
    print(content)

with open("new_file.txt", mode="w") as file:
    file.write("Adding this line to a new automatically created file.")
