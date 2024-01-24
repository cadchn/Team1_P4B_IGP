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


def sort_tuple(tup, truth):
    new_deficit_list = tup[:]
    new_deficit_list.sort(key = lambda x:x[1], reverse = truth)
    return new_deficit_list
# this part onwards should be in main.py file, have to also write the code to writelines in the summary report txt file in main.py file
sorted_deficit_list = sort_tuple(deficit_list, True)
sorted_surplus_list = sort_tuple(surplus_list, True)
# print(sorted_deficit_list)
# HD = sorted_deficit_list[0][0], sorted_deficit_list[0][1]
# SHD = sorted_deficit_list[1][0], sorted_deficit_list[1][1]
# THD = sorted_deficit_list[2][0], sorted_deficit_list[2][1]
# print(HD)
deficit_list.sort(key = lambda x:x[0], reverse = False)
# print(deficit_list)

if len(surplus_list) == len(difference_list):
    print(f"[CASH ON HAND SURPLUS] CASH ON HAND ON EACH DAY IS HIGHER THAN PREVIOUS DAY")
    print(f"[HIGHEST NET PROFIT SURPLUS] DAY: {sorted_surplus_list[0][0]}, AMOUNT: USD{sorted_surplus_list[0][1]}")
elif len(deficit_list) == len(difference_list):
    print("[CASH ON HAND SURPLUS] CASH ON HAND ON EACH DAY IS LOWER THAN PREVIOUS DAY")
    print(f"[HIGHEST CASH ON HAND DEFICIT] DAY: {sorted_deficit_list[0][0]}, AMOUNT: {sorted_deficit_list[0][1]}")
elif len(surplus_list) == 0 and len(deficit_list) == 0:
    print("are you even playing the game?")
else:
    for deficit in deficit_list:
        print(f"[CASH ON HAND DEFICIT] DAY: {deficit[0]}, AMOUNT: USD{deficit[1]}")
    print(f"[HIGHEST CASH ON HAND DEFICIT] DAY: {sorted_deficit_list[0][0]}, AMOUNT: {sorted_deficit_list[0][1]}")
    print(f"[2ND HIGHEST CASH ON HAND DEFICIT] DAY: {sorted_deficit_list[1][0]}, AMOUNT: {sorted_deficit_list[1][1]}")
    print(f"[3RD HIGHEST CASH ON HAND DEFICIT] DAY: {sorted_deficit_list[2][0]}, AMOUNT: {sorted_deficit_list[2][1]}")

for difference in difference_list:
    if difference[1] > 0:
        increase_list.append([difference[0], difference[1]])
# print(decrease_list)
