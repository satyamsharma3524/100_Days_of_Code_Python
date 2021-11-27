print('''
 _                                     
| |                                    
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ 
| __| '__/ _ \/ _` / __| | | | '__/ _ /
| |_| | |  __/ (_| \__ \ |_| | | |  __/
 \__|_|  \___|\__,_|___/\__,_|_|  \___| 
 _                 _   _             
| |               | | (_)            
| |__  _   _ _ __ | |_ _ _ __   __ _ 
| '_ \| | | | '_ \| __| | '_ \ / _` |
| | | | |_| | | | | |_| | | | | (_| |
|_| |_|\__,_|_| |_|\__|_|_| |_|\__, |
                                __/ |
                               |___/ 

''')

print("Welcome to the treasure hunting game.")
print("Your journey begins now : ")

choice1 = input('You are at a crossroad, Where do you want to go? type "left" or "right"\n').lower()

if choice1 == "left":
    choice2 = input('You have come across a lake, type "wait" to wait for a boat or type "swim" to swim over the lake.\n').lower()
    if choice2 == "wait":
        choice3 = input("You arrived at the island unharmed, There is a house with three doors, one Red, one Yellow and one Blue. Which door you want to choose? \n").lower()
        if choice3 == "red":
            print("You have entered in a room full of Spiders, Game over.")
        if choice3 == "yellow":
            print("Congratulations, You have found the treasure, You Win.")
        if choice3 == "blue":
            print("You have entered in the room of a Ghost, Game over.")
    else:
        print("You are attacked by the crocodiles in the lake, Game over.")
else:
    print("You fell into a pot hole, Game over.")
