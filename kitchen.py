
import csv

utensils = [
    ["name", "colour", "quantity"],
    ["spoon", "gold", 10],
    ["plates", "white", 50],
    ["cup", "black", 20],
    ["glass", "clear", 25],
    ["jug", "blue", 5],
    ["thermos", "purple", 1],
    ["fork", "silver", 28],
    ["knife", "silver", 10],
    ["bottle", "blue", 15],
    ["cooking pot", "black", 8]
]

with open("utensils.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(utensils)

print("CSV file saved")

