#this tip calculator is used to add some percentage of tip to the basic bill and then split the bill to required peoples.

# taking the amount of the total bill 
bill = int(input("Enter the amount of the bill : "))

# taking the amount of people in which the bill is to be splitted 
people = int(input("Enter the peoples to split bill : "))

# taking the tip percentage we want to add to the bill 
tip = float(input("Enter the tip you want to add : "))

# now we will calculate the total bill per person after adding the tip 
total_bill = bill+(bill/100)*tip
bill_per_person = round((total_bill/people),2)



print(f"The bill each person has to pay is : {bill_per_person}")