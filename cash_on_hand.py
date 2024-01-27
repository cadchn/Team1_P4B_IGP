from operator import itemgetter
from pathlib import Path
import csv

# create a file path to csv file.
fp = Path("cash_on_hand.csv")

# Read the csv file.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header 
    
    #read the data into array 
    cash_records = []
    for row in reader:
        cash_records.append([row[0],int(row[1])])

#Array to store the net profit difference 
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
cash_flow_flag = -1

counter = 1

# go through the list to find deficit and store in a deficit list
for difference in difference_list:    
    
    if counter < len(difference_list):
        
        if difference_list[counter][1] < difference[1]:
            deficit_list.append([difference_list[counter][0], difference_list[counter][2]])

    counter = counter + 1

# go through the list to find surplus and store in a surplus list
counter = 1
for difference in difference_list:    
    
    if counter < len(difference_list):

        if difference_list[counter][1] >= difference[1]:
            surplus_list.append([difference_list[counter][0], difference_list[counter][2]])

    counter = counter + 1


if len(surplus_list) == len(difference_list)-1:
    cash_flow_flag = 0 
    surplus_list.sort(key=itemgetter(1), reverse=True) #sort by descending order so that the largest surplus is the first in list
elif len(deficit_list) == len(difference_list)-1:
    cash_flow_flag =1 
    deficit_list.sort(key=itemgetter(1)) #sort by ascending order so that the largest deficit is the first in list
else:
    cash_flow_flag = 2 
    deficit_list.sort(key=itemgetter(1)) #sort by ascending order so that the largest deficit is the first in list

