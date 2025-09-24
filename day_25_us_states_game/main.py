# import csv

# with open("weather_data.csv") as f:
#     data = csv.reader(f)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
    
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# temperatures = data.temp.to_list()
# # print(temperatures)
# monday = data[data.day == "Monday"]
# temp = monday.temp[0]
# print(temp) 
# fahrenheit = (temp * 9/5) + 32
# print(fahrenheit) 

new_data = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 84]
}

data = pandas.DataFrame(new_data)
data.to_csv("new_data.csv")