import random

word_list = ["aardvark", "baboon", "camel"]

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)

# generating a blank list of ["_"] to store the number of guessed letters
guessed_letter = []
for letter in range(len(chosen_word)):
    guessed_letter.append("_")

print(guessed_letter)

# converting the string to a list 
def Convert(string):
    list1=[]
    list1[:0]=string
    return list1

chosen_word = Convert(chosen_word)
print(chosen_word)
# Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter : ").lower()
# Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for letter in chosen_word:
    var_letter = letter
    if guess == var_letter:
        print("true")
    else:
        print("false")