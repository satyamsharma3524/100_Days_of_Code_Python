# this variable has a global scope and it can be accessed from anywhere in the fucntion or outside the function 
enemies = 1

def increase_enemy():
    # this variable has a local scope and can only be accessed inside the function 
    enemies = 2
    print(f"the enemies inside the function are {enemies}")

increase_enemy()
print(f"The enemies outside the fucntion are {enemies}")