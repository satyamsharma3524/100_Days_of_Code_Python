import pandas

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

num_of_squirrels = squirrel_data['Primary Fur Color'].value_counts()
print(f"{num_of_squirrels}")

df = pandas.DataFrame(num_of_squirrels)
df.to_csv("Squirrel_colors.csv")

