name = input("What is your name?\n")
print_name = int(input("how many times you want to print your name?\n"))

# syntax of while loop 
while print_name>0:
    print(f"Hello {name}.")
    print_name-=1