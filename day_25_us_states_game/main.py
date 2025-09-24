import pandas as pd

f = pd.read_csv("squirel.csv")

datas = f.get(["Hectare Squirrel Number","Primary Fur Color"])

gray = datas[datas["Primary Fur Color"] == "Gray"]
cinnamon = datas[datas["Primary Fur Color"] == "Cinnamon"]
black = datas[datas["Primary Fur Color"] == "Black"]

gray_sum = sum(gray["Hectare Squirrel Number"])
cinnamon_sum = sum(cinnamon["Hectare Squirrel Number"])
black_sum = sum(black["Hectare Squirrel Number"])

new_data = {
    "Fur Color": ["gray", "red", "black"],
    "Count": [gray_sum, cinnamon_sum, black_sum]
}

new_file = pd.DataFrame(new_data)
new_file.to_csv("squirrel_count.csv")