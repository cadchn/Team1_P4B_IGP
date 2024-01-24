from pathlib import Path
import csv

file_path = Path (r"C:\Users\65962\OneDrive - Ngee Ann Polytechnic\Documents\p4b\cash_on_hand.csv")
with file_path.open(mode="r", encoding="UTF-8") as file:
    reader = csv.reader(file)
    next(reader)

    cash_on_hand = []
    for row in reader:
        cash_on_hand.append([int(row[0]), float(row[1])])

# print(cash_on_hand) 
difference_list = []
def difference_computation():
    '''
    This function finds the difference between the consecutive values of cash on hand column. 
    '''
    previous = 0
    for row in cash_on_hand:
        difference = row[1] - previous 
        previous = row[1] # previous variable will now be first index of preceding row
        difference_list.append([row[0],difference]) # appending all difference into an empty list
    return difference_list

difference_computation()

decrease_list = []
increase_list = []
for difference in difference_list:
    if difference[1] < 0:
        decrease_list.append([difference[0], difference[1]*-1])
for difference in difference_list:
    if difference[1] > 0:
        increase_list.append([difference[0], difference[1]])
# print(decrease_list)
