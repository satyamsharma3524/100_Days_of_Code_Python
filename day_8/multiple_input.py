def greet_with(name,location):
    print(f"Hello {name}!")
    print(f"How's the weather in {location}.")


name = input("Enter your name : \n")
location = input("What is your location : \n")

# Here name and location is positional arguments because if we switch their position the data that is passing to the fucntion also gets switched.
greet_with(name,location)