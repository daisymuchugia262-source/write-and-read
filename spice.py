
import csv

spices = [
    ["name", "price", "quantity"],
    ["black pepper", 150, 20],
    ["cinnamon", 120, 15],
    ["turmeric", 100, 25],
    ["paprika", 180, 12],
    ["ginger powder", 130, 18],
    ["garlic powder", 160, 10],
    ["cumin", 140, 14],
    ["coriander", 90, 22],
    ["chilli powder", 110, 16],
    ["cardamom", 200, 8]
]

with open("spices.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(spices)

print("CSV file saved")