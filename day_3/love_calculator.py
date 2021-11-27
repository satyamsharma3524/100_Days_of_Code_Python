print("Welcome to the love calculator.")
your_name = input("Enter your name : ").lower()
their_name = input("Enter their name : ").lower()

t = int(your_name.count("t")) + int(their_name.count("t"))
r = int(your_name.count("r")) + int(their_name.count("r"))
u = int(your_name.count("u")) + int(their_name.count("u"))
e = int(your_name.count("e")) + int(their_name.count("e"))

l = int(your_name.count("l")) + int(their_name.count("l"))
o = int(your_name.count("o")) + int(their_name.count("o"))
v = int(your_name.count("v")) + int(their_name.count("v"))
e = int(your_name.count("e")) + int(their_name.count("e"))

trues = t+r+u+e
loves = l+o+v+e

love_percent = int(str(trues)+str(loves))

if love_percent<10 or love_percent>90:
    print(f"Your score is {love_percent}, you go together like coke and mentos.")
elif love_percent>40 and love_percent<50:
    print(f"Your score is {love_percent}, you are alright together.")
else:
    print(f"Your score is {love_percent}.")