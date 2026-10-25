
import csv

shoes = [
    ["name", "size", "price", "quantity"],
    ["sneakers", 38, 2500, 15],
    ["boots", 40, 4000, 8],
    ["sandals", 37, 1000, 20],
    ["heels", 39, 2000, 10],
    ["loafers", 42, 3000, 12],
    ["slippers", 38, 500, 18],
    ["flats", 37, 1500, 14],
    ["sports shoes", 41, 3500, 11],
    ["school shoes", 40, 1800, 25],
    ["canvas shoes", 39, 2200, 16]
]

with open("shoes.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(shoes)

print("CSV file saved")
