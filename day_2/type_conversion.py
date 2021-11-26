name = input("enter your name : ")    # taking user input
length = len(name)                    # cheking the lenth of the characters
string_len = str(length)              # type-casting the length into string for concatination

print(type(length))                   # type() function is used to check the datatype of perticular value
print(type(string_len))
print("Your name has "+string_len+" characters")
