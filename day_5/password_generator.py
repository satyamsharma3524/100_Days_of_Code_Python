#Password Generator Project
import random
letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols_list = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator!")
letters= int(input("How many letters would you like in your password?\n")) 
symbols = int(input(f"How many symbols would you like?\n"))
numbers = int(input(f"How many numbers would you like?\n"))


# creating a array to store random letters 
letter1 = []
len_letters_list = len(letters_list)
for letter in range(letters):
    # generating random indexes from letter list 
    random_letter = random.randint(0,len_letters_list-1)
    letter1.append(letters_list[random_letter])


# creating a array to store random symbols 
symbol1 = []
len_symbols_list = len(symbols_list)
for letter in range(symbols):
    # generating random indexes from letter list 
    random_symbols = random.randint(0,len_symbols_list-1)
    symbol1.append(symbols_list[random_symbols])


# creating a array to store random numbers 
number1 = []
len_numbers_list = len(numbers_list)
for letter in range(numbers):
    # generating random indexes from letter list 
    random_numbers = random.randint(0,len_numbers_list-1)
    number1.append(numbers_list[random_numbers])


# creating main password list 
password = []
password = letter1 + symbol1 + number1
random.shuffle(password)

# joining all the elements in the list 
passwords = ''.join([str(elem) for elem in password])
print(f"Your password is : {passwords}")