
import csv

appliances = [
    ["name", "brand", "price", "power_watts"],
    ["kettle", "Ramtons", 2000, 1500],
    ["blender", "Von", 3500, 500],
    ["microwave", "Samsung", 12000, 1000],
    ["toaster", "Philips", 4000, 800],
    ["rice cooker", "Ramtons", 3000, 700],
    ["fridge", "LG", 45000, 200],
    ["oven", "Von", 15000, 2000],
    ["mixer", "Philips", 5000, 300],
    ["air fryer", "Nunix", 8000, 1500],
    ["sandwich maker", "Ramtons", 2500, 750]
]

with open("appliances.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(appliances)

print("CSV file saved")
