import csv
import os

# Files to load 
file= os.path.join("/Users/yxair/Desktop/NW Bootbcamps/HW/3-Python/Instructions/PyBank/Resources/budget_data.csv")
outputfile= os.path.join("/Users/yxair/Desktop/NW Bootbcamps/HW/3-Python/Instructions/PyBank/Resources/budget_analysis.txt")

count=0
net_change_list=[]
row_change=[]

greatest_ins_amount=["",0]
greatest_des_amount=["",99999999999999999999]
total_revenue=0
# Open csv file

with open (file) as bgtcsv:
       csvreader = csv.reader(bgtcsv)
       # For the first line
       header=next(csvreader)
       first_row=next(csvreader)
       count += 1
       total_revenue =int(first_row[1])
       previous_revenue=int(first_row[1])
       
       for row in csvreader:


               # The total number of months included in the dataset
              count=count+1

        # The net total amount of "Profit/Losses" over the entire period
              total_revenue+=int(row[1])
            
         
        # The average of the changes in "Profit/Losses" over the entire period
              change=int(row[1])-previous_revenue
              previous_revenue = int(row[1])
              net_change_list += [change]
              row_change += [row[0]]
              #total_changes=total_changes+change

        # The greatest increase in profits (date and amount) over the entire period
              if(change > greatest_ins_amount[1]):
                     greatest_ins_amount[0] = row[0]
                     greatest_ins_amount[1] = change

        # The greatest decrease in losses (date and amount) over the entire period
              if(change < greatest_des_amount[1]):
                     greatest_des_amount[0] = row[0]
                     greatest_des_amount[1] = change
         

avg_change=(sum(net_change_list)/len(net_change_list))

out= (
       f"Financial Analysis\n"
       "-------------------------------------------------------"
       f"Total Months: {count}\n"
       f"Total Revenue: {total_revenue}\n"
       f"Average Revenue Change: {avg_change:.2f}\n"
       f"Greatest Increase in Revenue: {greatest_ins_amount[0]} ${greatest_ins_amount[1]}\n"
       f"Greatest Decrease in Revenue: {greatest_des_amount[0]} ${greatest_des_amount[1]}\n"       
       "-------------------------------------------------------"

)


with open(outputfile, "w") as txt:
       txt.write(out)