import os
import csv 

budget_data_path = os.path.join(".." , "PyBank" , "budget_data.csv")

from csv import reader 

with open(budget_data_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    header = next(csvreader)
    
    for row in csvreader:
        row_count = sum(1 for row in csvreader) + 1
        print("Total Months:" + " " + str(row_count))
    
        #list_of_rows = list(csvreader)
        #print(list_of_rows)


        
        #if int(row[1]) > 1:
         #   print(row[1])
