from pathlib import Path
import csv

# Create a file path to csv file.
fp = Path("Overheads.csv")

# Read the csv file.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header 
    
    # Read the data into the list 
    overheads_records = []
    for row in reader:
        overheads_records.append([float(row[1]),row[0]]) 

# Sort the list based on the second column in descending order so that the largest overhead is the first in the array
overheads_records.sort(reverse=True)      
     
        
