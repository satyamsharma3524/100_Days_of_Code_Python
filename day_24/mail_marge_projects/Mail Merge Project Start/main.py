letter_file = open("./Input/Letters/starting_letter.txt", mode="r+")
names_file = open("./Input/Names/invited_names.txt", mode="r+")

letter = letter_file.read()

name = names_file.readlines()

for names in name:
    names.strip()
    new_letter = letter.replace("[name]", names)
    ready_to_send = open(f"./Output/ReadyToSend/letter_for_{names}.txt", mode="w")
    ready_to_send.write(new_letter)

