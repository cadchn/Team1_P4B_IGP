#--------------Import the modules that perform the different functions --------------#
import overheads
import profit_loss
import cash_on_hand
from pathlib import Path

txtfile = Path("summary_report.txt")
counter = 0

with open(txtfile, mode='w') as file:
    file.writelines("[HIGHEST OVERHEAD] " + f"{overheads.overheads_records[0][0]}" + ": " + f"{overheads.overheads_records[0][1]}" + "\n") 
    
    if cash_on_hand.cash_flow_flag == 0:
        file.writelines("[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN PREVIOUS DAY")
        file.writelines("[HIGHEST NET PROFIT SURPLUS] DAY: " + f"{cash_on_hand.surplus_list[0][0]}" + " AMOUNT: USD " + f"{cash_on_hand.surplus_list[0][1]}" )
    elif cash_on_hand.cash_flow_flag == 1:
        file.writelines("[NET PROFIT DEFICIT] NET PROFIT ON EACH DAY IS LOWER THAN PREVIOUS DAY")
        file.writelines("[HIGHEST NET PROFIT DEFICIT] DAY: " + f"{cash_on_hand.deficit_list[0][0]}" + " AMOUNT: USD " + f"{cash_on_hand.deficit_list[0][1]}" )
    elif cash_on_hand.cash_flow_flag == 2:
        for record in cash_on_hand.deficit_list:
            cash_on_hand.deficit_list.sort(key=itemgetter(0)) 
            file.writelines("[CASH DEFICIT] DAY: " + f"{record[0]}" + " AMOUNT: USD " + f"{record[1]}" + "\n")
        
        file.writelines("[HIGHEST CASH DEFICIT] DAY: " + f"{cash_on_hand.deficit_list[0][0]}" + " AMOUNT: USD " + f"{cash_on_hand.deficit_list[0][1]}" + "\n")
        file.writelines("[2ND HIGHEST CASH DEFICIT] DAY: " + f"{cash_on_hand.deficit_list[1][0]}" + " AMOUNT: USD " + f"{cash_on_hand.deficit_list[1][1]}" + "\n")
        file.writelines("[3RD HIGHEST CASH DEFICIT] DAY: " + f"{cash_on_hand.deficit_list[2][0]}" + " AMOUNT: USD " + f"{cash_on_hand.deficit_list[2][1]}" + "\n")
        cash_on_hand.deficit_list.sort(key=itemgetter(1)) 


    if profit_loss.profit_loss_flag == 0:
        file.writelines("[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN PREVIOUS DAY")
        file.writelines("[HIGHEST NET PROFIT SURPLUS] DAY: " + f"{profit_loss.surplus_list[0][0]}" + " AMOUNT: USD " + f"{profit_loss.surplus_list[0][1]}" )
    elif profit_loss.profit_loss_flag == 1:
        file.writelines("[NET PROFIT DEFICIT] NET PROFIT ON EACH DAY IS LOWER THAN PREVIOUS DAY")
        file.writelines("[HIGHEST NET PROFIT DEFICIT] DAY: " + f"{profit_loss.deficit_list[0][0]}" + " AMOUNT: USD " + f"{profit_loss.deficit_list[0][1]}" )
    elif profit_loss.profit_loss_flag == 2:
        for record in profit_loss.deficit_list:
            file.writelines("[NET PROFIT DEFICIT] DAY: " + f"{record[0]}" + " AMOUNT: USD " + f"{record[1]}" + "\n")
            profit_loss.deficit_list.sort(key=itemgetter(0)) to line 40
        
        file.writelines("[HIGHEST NET PROFIT DEFICIT] DAY: " + f"{profit_loss.deficit_list[0][0]}" + " AMOUNT: USD " + f"{profit_loss.deficit_list[0][1]}" + "\n")
        file.writelines("[2ND HIGHEST NET PROFIT DEFICIT] DAY: " + f"{profit_loss.deficit_list[1][0]}" + " AMOUNT: USD " + f"{profit_loss.deficit_list[1][1]}" + "\n")
        file.writelines("[3RD HIGHEST NET PROFIT DEFICIT] DAY: " + f"{profit_loss.deficit_list[2][0]}" + " AMOUNT: USD " + f"{profit_loss.deficit_list[2][1]}" + "\n")
        cash_on_hand.deficit_list.sort(key=itemgetter(1)) 
