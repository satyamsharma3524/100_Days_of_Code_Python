from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text,shift,directions):
    text = list(text)
    encrypted_data = []
    for character in text:
        if character in alphabet:
            index_of_character = alphabet.index(character)
            if directions == "encode":
                shifted = index_of_character + shift
            elif directions == "decode":
                shifted = index_of_character - shift
            else:
                print("You have entered an invalid Direction.")
            encrypted_data.append(alphabet[shifted])
            encrypted_string = "".join(encrypted_data)
        else:
            encrypted_data.append(character)
            encrypted_string = "".join(encrypted_data)
    
    print(f"The {directions}d text is {encrypted_string}")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number between 1 to 10:\n"))
    shift %= 26

    caesar(text=text,shift=shift,directions=direction)
    result = input("Type 'Yes' if you want to continue or type 'no' to exit.").lower()
    if result == "no":
        should_continue = False
        print("Good Bye.")