from pathlib import Path
import csv

# Create a file path to csv file.
fp = Path("cash_on_hand.csv")

# Read the csv file.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # Skip header row
    
    # Read the data into a list 
    cash_records = []
    for row in reader:
        cash_records.append([int(row[0]),int(row[1])])

# List is to store the net profit difference 
difference_list = []
def difference_computation():
    '''
    This function finds the difference between the consecutive values of net profit column. 
    '''
    previous = 0
    
    for row in cash_records:
        difference = row[1] - previous 
        previous = row[1] # previous variable will now be first index of preceding row
        difference_list.append([row[0],row[1], int(difference)]) # appending all difference into an empty list
        
    return difference_list
    
difference_computation()


#Find out if profit is increasing, decreasing or fluctuating
deficit_list = []
surplus_list = []
sorted_deficit_list = []
sorted_surplus_list = []
cash_flow_flag = -1

counter = 1 # Used to iterate through difference list

# go through the list to find deficit and store in a deficit list
for difference in difference_list:  # Starts a loop that iterates through each element (difference) through (difference_list)
    
    if counter < len(difference_list):
        
        if difference_list[counter][1] < difference[1]: 
            deficit_list.append([difference_list[counter][0], difference_list[counter][2]])
            sorted_deficit_list.append([difference_list[counter][2], difference_list[counter][0]])
            

    counter = counter + 1

# Go through the list to find surplus and store in a surplus list
counter = 1
for difference in difference_list:    
    
    if counter < len(difference_list):

        if difference_list[counter][1] >= difference[1]:
            surplus_list.append([difference_list[counter][0], difference_list[counter][2]])
            sorted_surplus_list.append([difference_list[counter][2], difference_list[counter][0]])

    counter = counter + 1


if len(surplus_list) == len(difference_list)-1: # Checks if surplus list is equal to one less than the length of difference list
    cash_flow_flag = 0
elif len(deficit_list) == len(difference_list)-1: # Checks if deficit list is equal to one less of difference list
    cash_flow_flag = 1
else:
    cash_flow_flag = 2
    

