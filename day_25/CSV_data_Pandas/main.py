import csv

temprature = []

with open("weather_data.csv") as CSV_data:
    data = csv.reader(CSV_data)

    for row in data:
        if row[1] != "temp":
            temprature.append(int(row[1]))

print(temprature)
