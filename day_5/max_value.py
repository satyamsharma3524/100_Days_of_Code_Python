scores = input("Input a list of student score : ").split()

# sorting the list so that the largest number will go to the last of the list
scores.sort()

# printing the largest last value of the list  
print("the maximum score is : " + scores[len(scores)-1])



# doing the same using for loop 
# heighest_value = 0

# for score in scores:
#     score = int(score)
#     if score > heighest_value:
#         heighest_value = score

# print(heighest_value)