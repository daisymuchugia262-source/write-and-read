
import csv

stationery = [
    ["name", "price", "quantity"],
    ["pen", 20, 50],
    ["pencil", 30, 40],
    ["notebook", 100, 25],
    ["ruler", 50, 20],
    ["eraser", 25, 30],
    ["marker", 150, 18],
    ["stapler", 400, 10],
    ["scissors", 200, 12],
    ["highlighter", 100, 15],
    ["exercise book", 80, 35]
]

with open("stationery.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(stationery)

print("CSV file saved")
