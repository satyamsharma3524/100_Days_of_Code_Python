def greet_with(name,location):
    print(f"Hello {name}!")
    print(f"How's the weather in {location}.")


names = input("Enter your name : \n")
locations = input("What is your location : \n")

# Here name and location is positional arguments because if we switch their position the data that is passing to the fucntion also gets switched.
greet_with(names,locations)

# Here name and location is keyword arguments because we have assigned a keyword to them during function call.
greet_with(name = names,location = locations)