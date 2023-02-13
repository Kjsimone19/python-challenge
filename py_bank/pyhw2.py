# Import csv
import os
import csv

# Declare path to csv
csvpath = os.path.join('.','Resources','budget_data.csv')

text_path = "output.txt"

#declare variables
total_months = 0
total_revenue = 0
revenue = []
prevRevenue = 0
changeMonth = []
revenue_change = 0
greatest_decrease = ["", 9999999]
greatest_increase = ["", 0]
revenue_change_list = []
revenue_average = 0

#use open command to read the .csv file
with open(csvpath) as csvFile:

    # set up the reader for the csv file
    csvReader = csv.reader(csvFile, delimiter=',')

    # read the row of headers- saves header as a variable and goes to the next line to start 
    csvHeader = next(csvReader)

    for row in csvReader:
    
        #count total months 
        total_months += 1
        
        #calculate revenue
        total_revenue = total_revenue + int(row[1])

        #Calculate the average change in revenue (over entire file)
        revenue_change = float(row[1])- prevRevenue
        prevRevenue = float(row[1])
        revenue_change_list += [revenue_change]
        changeMonth += [row[0]]

        #Find greatest increase 
        if revenue_change>greatest_increase[1]:
              greatest_increase[1]= revenue_change
              greatest_increase[0] = row[0]

        #Find greatest decrease
        if revenue_change<greatest_decrease[1]:
              greatest_decrease[1]= revenue_change
              greatest_decrease[0] = row[0]
        
    revenue_change_list = revenue_change_list[1:]
    revenue_average = sum(revenue_change_list)/len(revenue_change_list)


    print("Financial Analysis")
    print("---------------------")
    print("Total Months: %d\n" % total_months)
    print("Total Revenue: $%d\n" % total_revenue)
    print("Average Revenue Change $%d\n" % revenue_average)
    print("Greatest Increase in Revenue: %s ($%s)\n" % (greatest_increase[0], greatest_increase[1]))
    print("Greatest Decrease in Revenue: %s ($%s)\n" % (greatest_decrease[0], greatest_decrease[1]))

    #export to texy file 
with open(text_path, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("---------------------\n")
    file.write("Total Months: %d\n" % total_months)
    file.write("Total Revenue: $%d\n" % total_revenue)
    file.write("Average Revenue Change $%d\n" % revenue_average)
    file.write("Greatest Increase in Revenue: %s ($%s)\n" % (greatest_increase[0], greatest_increase[1]))
    file.write("Greatest Decrease in Revenue: %s ($%s)\n" % (greatest_decrease[0], greatest_decrease[1]))