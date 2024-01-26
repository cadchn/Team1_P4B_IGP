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
    This function finds the difference between the consecutive values of net profit column. 
    '''
    previous = 0
    
    for row in cash_on_hand:
        difference = row[1] - previous 
        previous = row[1] # previous variable will now be first index of preceding row
        difference_list.append([row[0],difference]) # appending all difference into an empty list
    return difference_list

difference_computation()

deficit_list = []
sorted_deficit_list = []
surplus_list = []
sorted_surplus_list = []
for difference in difference_list:
    if difference[1] < 0:
        deficit_list.append([difference[0], difference[1]*-1])
        sorted_deficit_list.append([difference[1]*-1, difference[0]])
for difference in difference_list:
    if difference[1] > 0:
        surplus_list.append([difference[0], difference[1]])
        sorted_surplus_list.append([difference[1], difference[0]])

sorted_deficit_list.sort(reverse=True)
sorted_surplus_list.sort(reverse=True)

if len(surplus_list) == len(difference_list):
    print(f"[NET PROFIT SURPLUS] CASH ON HAND ON EACH DAY IS HIGHER THAN PREVIOUS DAY")
    print(f"[HIGHEST NET PROFIT SURPLUS] DAY: {sorted_surplus_list[0][1]}, AMOUNT: USD{sorted_surplus_list[0][0]}")
elif len(deficit_list) == len(difference_list):
    print("[NET PROFIT SURPLUS] CASH ON HAND ON EACH DAY IS LOWER THAN PREVIOUS DAY")
    print(f"[HIGHEST NET PROFIT DEFICIT] DAY: {sorted_deficit_list[0][1]}, AMOUNT: {sorted_deficit_list[0][0]}")
elif len(surplus_list) == 0 and len(deficit_list) == 0:
    print("are you even playing the game?")
else:
    for deficit in deficit_list:
        print(f"[CASH ON HAND DEFICIT] DAY: {deficit[0]}, AMOUNT: USD{deficit[1]}")
    print(f"[HIGHEST CASH ON HAND DEFICIT] DAY: {sorted_deficit_list[0][1]}, AMOUNT: {sorted_deficit_list[0][0]}")
    print(f"[2ND HIGHEST CASH ON HAND DEFICIT] DAY: {sorted_deficit_list[1][1]}, AMOUNT: {sorted_deficit_list[1][0]}")
    print(f"[3RD HIGHEST CASH ON HAND DEFICIT] DAY: {sorted_deficit_list[2][1]}, AMOUNT: {sorted_deficit_list[2][0]}")
