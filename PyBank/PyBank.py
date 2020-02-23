import os
import csv 

budget_data_path = os.path.join(".." , "PyBank" , "budget_data.csv")

from csv import reader 

with open(budget_data_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # skips header and moves through csv file 
    header = next(csvreader)
   
    # sets total to 0 so that the preceding numbers having a starting point to add to
    total = 0

    # creates lists of the revenue aka row values, changes in revenues from row to row, and the dates which act as placemark 
    revenue = []
    revenue_change = []
    date = []

    # read and loops through the csv file 
    for row in csvreader:
        
        # adds the amount of consective row values to total 
        total = total + int(row[1])
        
        #appends values in row[1] aka revenues to revenue list 
        revenue.append(float(row[1]))
        #appends values in row[0] aka dates to date list 
        date.append(row[0])

    print("Financial Analysis")     #formatting
    print("----------------------------")       #formatting
    
    # prints the length of the cells in csv, -1 to not include the header 
    print("Total Months: " + str(len(list(csv.reader(open(budget_data_path))))-1))
    
    # prints sum of all revenue values
    print("Total: " + str(total))
    
    #loops through all of values in revenue list
    for i in range(1,len(revenue)):
        
        #appends the differences in subsequent rows to the revenue change list 
        revenue_change.append(revenue[i] - revenue[i-1])

        #defines & calculates average revenue change as the sum of the each differnce in revenues divided by the total amount of values in revenue change list
        average_revenue_change = sum(revenue_change)/len(revenue_change)

        #defines max revenue change as the largest revenue change in the list of revenue changes
        max_revenue_change = max(revenue_change)

        #defines min revenue change as the smalles revenue change in the list of revenue changes
        min_revenue_change = min(revenue_change)

        #takes the max revenue change and index from the appended date list and defines as max_revenue_change_date
        max_revenue_change_date = str(date[revenue_change.index(max(revenue_change))])
        
        #takes the min revenue change and index from the appended date list and defines as min_revenue_change_date
        min_revenue_change_date = str(date[revenue_change.index(min(revenue_change))])
    
    #prints the average revenue change calculated in line 49 
    print("Average Revenue Change: $", float(average_revenue_change))

    #prints the date associated with the max value in list of revenue changes along with its respective revenue change value
    print("Greatest Increase in Revenue:", max_revenue_change_date,"($", max_revenue_change,")")
    
    #prints the date associated with the min value in list of revenue changes along with its respective revenue change value
    print("Greatest Decrease in Revenue:", min_revenue_change_date,"($", min_revenue_change,")")

    output_file = os.path.join('Financial_analysis.txt')
    with open(output_file,"w") as txt_file:
        output_file.write("Saving to text file")

    