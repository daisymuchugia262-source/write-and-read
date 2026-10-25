
import csv

cleaning = [
    ["name", "brand", "price"],
    ["detergent", "Sunlight", 250],
    ["bleach", "Jik", 180],
    ["dishwashing liquid", "Morning Fresh", 200],
    ["disinfectant", "Dettol", 350],
    ["sponge", "Scotch-Brite", 100],
    ["broom", "Generic", 250],
    ["mop", "Generic", 600],
    ["bucket", "Generic", 300],
    ["toilet cleaner", "Harpic", 250],
    ["floor cleaner", "Mr Muscle", 400]
]

with open("cleaning.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(cleaning)

print("CSV file saved")
