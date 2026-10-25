
import csv

beauty = [
    ["name", "brand", "price", "skin_type"],
    ["lipstick", "Maybelline", 800, "All"],
    ["foundation", "L'Oreal", 1500, "All"],
    ["mascara", "Maybelline", 900, "All"],
    ["face powder", "Black Opal", 1200, "Oily"],
    ["lip gloss", "NYX", 700, "All"],
    ["nail polish", "Essence", 300, "All"],
    ["body lotion", "Nivea", 600, "Dry"],
    ["sunscreen", "Garnier", 1000, "All"],
    ["perfume", "Lattafa", 2500, "All"],
    ["face wash", "CeraVe", 1800, "All"]
]

with open("beauty.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(beauty)

print("CSV file saved")
