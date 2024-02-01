from pathlib import Path
import csv

'''
Read data from file into array
'''
file_path = Path("profit_and_loss.csv")
with file_path.open(mode="r", encoding="UTF-8") as file:
    reader = csv.reader(file)
    next(reader)

    profit_loss = []
    for row in reader:
        profit_loss.append([int(row[0]), float(row[4])]) #read first and last column into the array.


# Array to store the net profit difference 
difference_list = []
def difference_computation():
    '''
    This function finds the difference between the consecutive values of net profit column. 
    '''
    previous = 0
    
    for row in profit_loss:
        difference = row[1] - previous 
        previous = row[1] # previous variable will now be first index of preceding row
        difference_list.append([row[0], int(row[1]), int(difference)]) # appending day, net profit and the difference into an empty list
        
    return difference_list
    
difference_computation()


# Find out if profit is increasing, decreasing or fluctuating
deficit_list = []
surplus_list = []
sorted_deficit_list = []
sorted_surplus_list = []
profit_loss_flag = -1

counter = 1 # Used to iterate through difference list

# Go through the list to find deficit and store in a deficit list
for difference in difference_list:    
    
    if counter < len(difference_list):
        
        if difference_list[counter][1] < difference[1]:
            deficit_list.append([difference_list[counter][0], difference_list[counter][2]]) #append by day field
            sorted_deficit_list.append([difference_list[counter][2], difference_list[counter][0]]) #append by deficit value field

    counter = counter + 1

# Go through the list to find surplus and store in surplus list
counter = 1
for difference in difference_list:    
    
    if counter < len(difference_list):

        if difference_list[counter][1] >= difference[1]:
            surplus_list.append([difference_list[counter][0], difference_list[counter][2]]) #append by day field
            sorted_surplus_list.append([difference_list[counter][2], difference_list[counter][0]]) #append by surplus value field

    counter = counter + 1


if len(surplus_list) == len(difference_list)-1: # Checks if surplus list is equal to one less than the length of difference list
    profit_loss_flag = 0
elif len(deficit_list) == len(difference_list)-1: # Checks if deficit list is equal to one less of difference list
    profit_lost_flag = 1
else:
    profit_loss_flag = 2
    