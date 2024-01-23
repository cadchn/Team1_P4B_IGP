from pathlib import Path
import csv

file_path = Path(r"C:\Users\jocel\PFB IGP\Team1_P4B_IGP\profit_and_loss.csv")

with file_path.open(mode="r", encoding="UTF-8") as file:
    reader = csv.reader(file)
    next(reader)

    profit_loss = []
    for row in reader:
        profit_loss.append([int(row[0]), float(row[4])])

# print(profit_loss) 
difference_list = []
def difference_computation():
    '''
    This function finds the difference between the consecutive values of net profit column. 
    '''
    previous = 0
    
    for row in profit_loss:
        difference = row[1] - previous 
        previous = row[1] # previous variable will now be first index of preceding row
        difference_list.append([row[0],difference]) # appending all difference into an empty list
    return difference_list
    
print(difference_computation())

# from here onwards, idk if need, but this is a desparate attempt to find out always increasing, decreasing or fluctuating
deficit_list = []
surplus_list = []
for difference in difference_list:
    if difference[1] < 0:
        deficit_list.append([difference[0], difference[1]*-1])
for difference in difference_list:
    if difference[1] > 0:
        surplus_list.append([difference[0], difference[1]])
print(deficit_list)

def sort_tuple(tup, truth):
    tup.sort(key = lambda x: x[0], reverse = truth)
    return tup

sorted_deficit_list = sort_tuple(deficit_list, False)
sorted_surplus_list = sort_tuple(surplus_list, True)



if len(surplus_list) == len(difference_list):
    print(f"[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN PREVIOUS DAY")
    print(f"[HIGHEST NET PROFIT SURPLUS] DAY: {sorted_surplus_list[0][0]}, AMOUNT: USD{sorted_surplus_list[0][1]}")
elif len(deficit_list) == len(difference_list):
    print("[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS LOWER THAN PREVIOUS DAY")
    print(f"[HIGHEST NET PROFIT DEFICIT] DAY: {sorted_deficit_list[0][0]}, AMOUNT: {sorted_deficit_list[0][1]}")
elif len(surplus_list) == 0 and len(deficit_list) == 0:
    print("are you even playing the game?")
else:
    for deficit in deficit_list:
        print(f"[NET PROFIT DEFICIT] DAY: {deficit[0]}, AMOUNT: USD{deficit[1]}")
    print(f"[HIGHEST NET PROFIT DEFICIT] DAY: {sorted_deficit_list[0][0]}, AMOUNT: {sorted_deficit_list[0][1]}")
    print(f"[2ND HIGHEST NET PROFIT DEFICIT] DAY: {sorted_deficit_list[1][0]}, AMOUNT: {sorted_deficit_list[1][1]}")
    print(f"[3RD HIGHEST NET PROFIT DEFICIT] DAY: {sorted_deficit_list[2][0]}, AMOUNT: {sorted_deficit_list[2][1]}")

