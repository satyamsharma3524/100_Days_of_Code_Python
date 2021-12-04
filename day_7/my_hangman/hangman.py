import random
import hangman_art
import hangman_words

print(hangman_art.logo)

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(hangman_words.word_list)

print(f"The solution is {chosen_word}")
# converting the string to a list 
def Convert(string):
    list1=[]
    list1[:0]=string
    return list1

# converting the randomly computer chosen word to a list 
chosen_word = Convert(chosen_word)

# generating a blank list of ["_"] to store the number of user guessed letters
guessed_letter = []
for letter in range(len(chosen_word)):
    guessed_letter.append("_")


# creating a lives variable to keep track of the user's lives. '
lives = 6

end_of_game = False
while not end_of_game:
  # Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
  guess = input("Guess a letter : ").lower()

  if guess in guessed_letter:
        print(f"you have already guessed this lettter {guess}")

  # Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
  for position in range(len(chosen_word)):
      letter = chosen_word[position]
      if guess == letter:
          guessed_letter[position] = letter
      
  if guess not in chosen_word:
    print(f"You guesses {guess}, that is not in the word. You loose a life.")
    lives -= 1
    if lives == 0:
        end_of_game = True
        print("You loose")
         
  print(guessed_letter)

    #Check if user has got all letters.
  if "_" not in guessed_letter:
    end_of_game = True
    print("You win.")

  print(hangman_art.stages[lives])