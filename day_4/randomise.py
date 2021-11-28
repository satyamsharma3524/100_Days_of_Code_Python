import random

# creating random integer value 
random_integer = random.randint(1,10)
print("The random integer number between 0 to 10 is : "+str(random_integer))

# creating random floating point value 
random_float = random.random()
print("The random float number between 0 to 1 is : "+str(random_float))

#if we want to take the value of random float instead of (0-1) to (0-5) then we just have to multiply the value of random by 5 or anything we want the range to be...
random_float *= 5
print("The random float number between 0 to 5 is : "+str(random_float))
