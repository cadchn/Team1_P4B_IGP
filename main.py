#--------------Import the modules that perform the different functions --------------#
import overheads
import profit_loss
import cash_on_hand
from pathlib import Path

txtfile = Path("summary_report.txt")
counter = 0

with open(txtfile, mode='w') as file:
    file.writelines("[HIGHEST OVERHEAD] " + f"{overheads.overheads_records[0][1]}" + ": " + f"{overheads.overheads_records[0][0]}" + "% \n") 
    
    if cash_on_hand.cash_flow_flag == 0:
        cash_on_hand.sorted_surplus_list.sort(reverse=True)
        file.writelines("[CASH SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN PREVIOUS DAY")
        file.writelines("[HIGHEST CASH SURPLUS] DAY: " + f"{cash_on_hand.sorted_surplus_list[0][1]}" + " AMOUNT: USD " + f"{abs(cash_on_hand.sorted_surplus_list[0][0])}" )
    elif cash_on_hand.cash_flow_flag == 1:
        cash_on_hand.sorted_deficit_list.sort(reverse=True)      
        file.writelines("[CASH DEFICIT] NET PROFIT ON EACH DAY IS LOWER THAN PREVIOUS DAY")
        file.writelines("[HIGHEST CASH DEFICIT] DAY: " + f"{cash_on_hand.sorted_deficit_list[0][1]}" + " AMOUNT: USD " + f"{abs(cash_on_hand.sorted_deficit_list[0][0])}" )
    
    elif cash_on_hand.cash_flow_flag == 2:
        cash_on_hand.deficit_list.sort(reverse=False) # sort by day
        for record in cash_on_hand.deficit_list:
            file.writelines("[CASH DEFICIT] DAY: " + f"{record[0]}" + " AMOUNT: USD " + f"{abs(record[1])}" + "\n")
        
        cash_on_hand.sorted_deficit_list.sort(reverse=False)
        file.writelines("[HIGHEST CASH DEFICIT] DAY: " + f"{cash_on_hand.sorted_deficit_list[0][1]}" + " AMOUNT: USD " + f"{abs(cash_on_hand.sorted_deficit_list[0][0])}" + "\n")
        file.writelines("[2ND HIGHEST CASH DEFICIT] DAY: " + f"{cash_on_hand.sorted_deficit_list[1][1]}" + " AMOUNT: USD " + f"{abs(cash_on_hand.sorted_deficit_list[1][0])}" + "\n")
        file.writelines("[3RD HIGHEST CASH DEFICIT] DAY: " + f"{cash_on_hand.sorted_deficit_list[2][1]}" + " AMOUNT: USD " + f"{abs(cash_on_hand.sorted_deficit_list[2][0])}" + "\n")
        


    if profit_loss.profit_loss_flag == 0: #net profit on each day is higher than previous day
        profit_loss.sorted_surplus_list.sort(reverse=True)
        file.writelines("[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN PREVIOUS DAY")
        file.writelines("[HIGHEST NET PROFIT SURPLUS] DAY: " + f"{profit_loss.surplus_list[0][0]}" + " AMOUNT: USD " + f"{abs(profit_loss.surplus_list[0][1])}" )
    
    elif profit_loss.profit_loss_flag == 1: # net profit on each day is lower than previous day
        profit_loss.sorted_deficit_list.sort(reverse=True)
        file.writelines("[NET PROFIT DEFICIT] NET PROFIT ON EACH DAY IS LOWER THAN PREVIOUS DAY")
        file.writelines("[HIGHEST NET PROFIT DEFICIT] DAY: " + f"{profit_loss.deficit_list[0][0]}" + " AMOUNT: USD " + f"{abs(profit_loss.deficit_list[0][1])}" )
    
    elif profit_loss.profit_loss_flag == 2: # net profit fluctuate
        profit_loss.deficit_list.sort(reverse=False) # sort by day
        for record in profit_loss.deficit_list:
            file.writelines("[NET PROFIT DEFICIT] DAY: " + f"{record[0]}" + " AMOUNT: USD " + f"{abs(record[1])}" + "\n")
        
        profit_loss.sorted_deficit_list.sort(reverse=False) #sort by amount
        file.writelines("[HIGHEST NET PROFIT DEFICIT] DAY: " + f"{profit_loss.sorted_deficit_list[0][1]}" + " AMOUNT: USD " + f"{abs(profit_loss.sorted_deficit_list[0][0])}" + "\n")
        file.writelines("[2ND HIGHEST NET PROFIT DEFICIT] DAY: " + f"{profit_loss.sorted_deficit_list[1][1]}" + " AMOUNT: USD " + f"{abs(profit_loss.sorted_deficit_list[1][0])}" + "\n")
        file.writelines("[3RD HIGHEST NET PROFIT DEFICIT] DAY: " + f"{profit_loss.sorted_deficit_list[2][1]}" + " AMOUNT: USD " + f"{abs(profit_loss.sorted_deficit_list[2][0])}" + "\n")
        
        
