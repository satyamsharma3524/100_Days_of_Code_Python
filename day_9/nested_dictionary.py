# Normal Dictionary 
Capitals = {
    "India":"Delhi",
    "France":"Paris",
    "germany":"Berlin",
}

# Nesting a list in a dictionary 
travel_log = {
    "India" : ["Delhi","Mumbai","Chandigarh","Bangalore"],
    "France" : ["Paris","Lille","Dijon"],
    "Germany" : ["Berlin","Hamburg","Stuttgart"],
}

# Nesting a dictionary in a dictionary 
travel_log = {
    "India" : {"cities_visited":["Delhi","Mumbai","Chandigarh","Bangalore"],"total_visits" : 9},
    "France" : {"cities_visited":["Paris","Lille","Dijon"],"total_visits" : 6},
    "Germany" : {"cities_visited":["Berlin","Hamburg","Stuttgart"],"total_visits" : 4},
}

# nesting a dictionary in a list 
travel_log = [
    {"country":"India",
    "cities_visited":["Delhi","Mumbai","Chandigarh","Bangalore"],
    "total_visits" : 9
    },
    {"country":"France",
    "cities_visited":["Paris","Lille","Dijon"],
    "total_visits" : 6
    },
    {"country":"Germany",
    "cities_visited":["Berlin","Hamburg","Stuttgart"],
    "total_visits" : 4
    },
]
