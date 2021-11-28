import random   #importing the random module to create the random numbers

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for scissors."))

valid_choices = [rock, paper, scissors]

computer_choice = random.randint(0,2)

if computer_choice == 0:
    print("computer's Choice : Rock")
    print(rock)
elif computer_choice == 1:
    print("computer's Choice : Paper")
    print(paper)
else:
    print("computer's Choice : Scissors")
    print(scissors)

if user_choice == 0:
    print("Your Choice : Rock")
    print(rock)
elif user_choice == 1:
    print("Your Choice : Paper")
    print(paper)
elif user_choice ==2:
    print("computer's Choice : Scissors")
    print(scissors)
else:
    print("You have entered an invalid number, You loose!")

if computer_choice == user_choice:
    print('This is a draw.')
elif computer_choice == 0 and user_choice == 1:
    print("Congratulations! You win.")
elif computer_choice == 1 and user_choice == 2:
    print("Congratulations! You win.")
elif computer_choice == 2 and user_choice == 0:
    print("Congratulations! You win.")
elif computer_choice == 1 and user_choice == 0:
    print("Alas! You loose.")
elif computer_choice == 2 and user_choice == 1:
    print("Alas! You loose.")
elif computer_choice == 0 and user_choice == 2:
    print("Alas! You loose.")
else:
    print("You are very dumb.")