import csv
import os

# Files to load 
file= os.path.join("/Users/yxair/Desktop/NW Bootbcamps/HW/3-Python/Instructions/PyBank/Resources/budget_data.csv")

count=0
revenue=[]
row_change=[]
total_revenue=0
change=[]
total_changes=0
greatest_ins_amount=0
greatest_des_amount=0
ins_date="Date"
des_date="Date"

# Open csv file

with open (file, newline='') as bgtcsv:
     csvreader = csv.reader(bgtcsv, delimiter=',')
     

     for row in csvreader:
         row = next(csvreader,None)
         

        # The total number of months included in the dataset
         count=count+1

        # The net total amount of "Profit/Losses" over the entire period
         revenue=int(row[1])
         total_revenue=total_revenue+revenue
         
        # The average of the changes in "Profit/Losses" over the entire period
         previous_revenue=revenue
         change=revenue-previous_revenue
         total_changes=total_changes+change


         avg_change=(total_changes/count)
         previous_revenue=revenue

        # The greatest increase in profits (date and amount) over the entire period
        #  greatest_ins_amount=max([change])
        #  ins_date = row[0:[change].index(greatest_ins_amount)]
         if(change > greatest_ins_amount):
                greatest_ins_amount = change
                ins_date = row[0]

        # The greatest decrease in losses (date and amount) over the entire period
        #  greatest_des_amount=min([change])
        #  des_date = row[0:[change].index(greatest_des_amount)]
         if(change < greatest_des_amount):
                greatest_des_amount = change
                des_date = row[0]
         


         print(f"Financial Analysis")
         print("-------------------------------------------------------")
         print(f"Total Months: {count}")
         print(f"Total Revenue: {total_revenue}")
         print(f"Average Revenue Change: {avg_change}")
         print(f"Greatest Increase in Revenue: {ins_date} {greatest_ins_amount}")
         print(f"Greatest Decrease in Revenue: {des_date} {greatest_des_amount}")        
         print("-------------------------------------------------------")