from pathlib import Path
import csv

file_path = Path("profit_and_loss.csv")

with file_path.open(mode="r", encoding="UTF-8") as file:
    reader = csv.reader(file)
    next(reader)

    profit_loss = []
    for row in reader:
        profit_loss.append([row[0], float(row[4])])

# print(profit_loss)
        