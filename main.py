#####  Name, email, student_id and class_number as STRINGS #####
#assignment = "My Final Year Assignment"
#name = Caden_Chan
#np_email = s10256040@connect.np.edu.sg
#student_id = S10256040
#class_number = TF02

#--------------Import the modules that perform the different functions --------------#
import overheads
import profit_loss
import cash_on_hand
from pathlib import Path

txtfile = Path("summary_report.txt")

if txtfile.exists():
    # 1. Write the highest overhead info to the summary report file. Name it as summary_report.txt.
    with open(txtfile, mode='a') as file:
        file.writelines("[HIGHEST OVERHEAD] " + f"{overheads.overheads_records[0][0]}" + " " + f"{overheads.overheads_records[0][1]}" + "\n")
else:
    with open(txtfile, mode='w') as file:
        file.writelines("[HIGHEST OVERHEAD] " + f"{overheads.overheads_records[0][0]}" + " " + f"{overheads.overheads_records[0][1]}" + "\n")

