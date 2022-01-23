import pandas
import pandas as pd

data = pd.read_csv("weather_data.csv")
print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

data_list = data["temp"].to_list()
print(f"The data list is : {data_list}")

print(f"This is the average of the temp list: {data['temp'].mean()}")

print(f"This is the Maximum of the temp list: {data['temp'].max()}")


# get data in column
print(data["condition"])
print(data.condition)

# get data in row
print(data[data.temp == data.temp.max()])

# getting the temperature of monday in Fahrenheit
monday = data[data.day == "Monday"]
temp_in_F = (int(monday.temp) * 9/5) + 32
print(f"temperature of monday in Fahrenheit : {temp_in_F}")

# creating a dataframe from scratch in python
frame_data = {
    "student" : ["satyam", "shivam", "roshni"],
    "scores" : ["76", "56", "65"]
}
datas = pandas.DataFrame(frame_data)
datas.to_csv("new_data.csv")
