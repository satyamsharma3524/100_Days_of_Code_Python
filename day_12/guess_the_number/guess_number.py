from art import logo
import random,click

def game():
    print(logo)
    def guess_the_number():
        """This function gives a random computer genarated number"""
        print("I am thinking a number between 1 to 100.")
        computer_guess = random.randint(1,100)
        return computer_guess

    lives_remaining = True
    level = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
    if level=="easy":
        lives = 10
    else:
        lives = 5

    computer_guess = guess_the_number()

    while lives_remaining:
        print(f"you have {lives} attempts to guess the number.")
        user_guess = int(input("Guess a number : "))
        if computer_guess == user_guess:
            print("congratulations! You guesses it right.")
            play_again = input("Play again? Type 'y' to start or press 'n'.").lower()
            if play_again=="y":
                click.clear()
                game()
            else:
                print("Good Bye! Have a nice day.")
                break
                
        elif computer_guess > user_guess:
            print("Too low\nGuess again.")
        elif computer_guess < user_guess:
            print("Too high\nGuess again.")
        lives -= 1
        if lives == 0:
            lives_remaining = False
            print("You run out of chances, You loose.")

game()