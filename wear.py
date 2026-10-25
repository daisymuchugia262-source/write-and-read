
import csv

clothes = [
    ["name", "size", "price", "quantity"],
    ["shirt", "M", 800, 20],
    ["trousers", "L", 1500, 15],
    ["dress", "S", 1200, 10],
    ["skirt", "M", 900, 12],
    ["jacket", "L", 2500, 8],
    ["sweater", "M", 1800, 14],
    ["shorts", "S", 700, 18],
    ["socks", "Free size", 200, 30],
    ["hoodie", "L", 2000, 9],
    ["T-shirt", "M", 600, 25]
]

with open("clothes.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(clothes)

print("CSV file saved")
