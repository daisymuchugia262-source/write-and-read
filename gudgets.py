
import csv

electronics = [
    ["name", "brand", "price"],
    ["laptop", "HP", 45000],
    ["phone", "Samsung", 25000],
    ["keyboard", "Logitech", 2000],
    ["mouse", "HP", 1000],
    ["speaker", "JBL", 5000],
    ["headphones", "Sony", 3500],
    ["charger", "Samsung", 1500],
    ["power bank", "Oraimo", 2500],
    ["flash disk", "SanDisk", 800],
    ["tablet", "Lenovo", 18000]
]

with open("electronics.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(electronics)

print("CSV file saved")
