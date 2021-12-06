animal_dictionary = {
    "Lion":"Lion is the king of jungle.",
    "Cats":"Cats are very cute.",
    "Dogs":"Dogs are very loyal and Friendly.",
}

# printing the item from a dictionary 
print(animal_dictionary["Lion"])

# adding new data to the dictionary 
animal_dictionary["Birds"] = "Birds are the cute flying creatures."
print(animal_dictionary["Birds"])

# Edit the data in a dictionary. 
animal_dictionary["Dogs"] = "Doggo are very loyal and Friendly"
print(animal_dictionary["Dogs"])

# wiping the data from a dictionary ad make it empty.
animal_dictionary = {}
print(animal_dictionary)