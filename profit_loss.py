from operator import itemgetter
from pathlib import Path
import csv

'''
Read data from file into array
'''
file_path = Path(r"profit_and_loss.csv")
with file_path.open(mode="r", encoding="UTF-8") as file:
    reader = csv.reader(file)
    next(reader)

    profit_loss = []
    for row in reader:
        profit_loss.append([int(row[0]), float(row[4])]) #read first and last column into the array.


#Array to store the net profit difference 
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
def sort_the_array_column_wise(arr):
    x = 1
    for x in range (len(arr)):
        #for y in range(len(arr) - 1):
        if arr[x-1][1] >= arr[x][1]:
            temp = arr[x-1][1]
            arr[x-1][1] = arr[x][1]
            arr[x][1] = temp

    for record in arr:
        print(record)

#Find out if profit is increasing, decreasing or fluctuating
deficit_list = []
surplus_list = []
profit_loss_flag = -1

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
    profit_loss_flag = 0
    surplus_list.sort(key=itemgetter(1), reverse=True) #sort by descending order so that the largest surplus is the first in list
elif len(deficit_list) == len(difference_list)-1:
    profit_lost_flag = 1
    deficit_list.sort(key=itemgetter(1)) #sort by ascending order so that the largest deficit is the first in list
else:
    profit_loss_flag = 2
    deficit_list.sort(key=itemgetter(1)) #sort by ascending order so that the largest deficit is the first in list

    
file_path = Path(r"summary_report.txt")
with file_path.open(mode="w", encoding="UTF-8") as file:
  file.write("All days and amount when deficit occured")
  file.close()
