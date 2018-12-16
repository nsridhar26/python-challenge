import os
import csv
#relative path of CSV file
file_to_load = os.path.join("Pybank","budget_data.csv")
#file_to_output = os.path.join("Analysis", "budget_analysis.txt")?
#open and read csv
with open(file_to_load, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    cvs_header = next(reader)
    # read the header row first
    print(f"Header: {csv_header}")
    num_lines = 0
    # read through each row of data after the header
    for row in csvreader:
#skip the data in the header
        row = next(reader)
        num_lines += 1
    print("Number of months:")
    print(num_lines)
#print number of months in the data set
#fname = input("file_to_load: ")
        
#with open(fname, 'r') as f:
    #for line in f:
        

#calculate the amount of revenue
# create a for loop that grabs the second column and prints the sum
revenue = 0
for row in csvreader:
    revenue += float(row[2])
    print("net amount of Profit/Losses ")
    print(revenue)
#average change in "profit/Losses"
for row in csvreader:
    avg_change = 0
    avg_change = ((row -(row-1))/2)
    avg_change += avg_change
#append avg_change to csv file
csvfile.append(avg_change)
print("Average Change: $")
print(avg_change)
#calculate the greatest increase in profits (date and amount) over the entire period
""" for row in csvreader
    #max_avg_change=(avg_change)
    # date of max avg change
    date_max_avg_change=row(max_avg_change[row(0)])
        print("Greatest Increase in Profits: ")
        print(date_max_avg_change)
        print(max_avg_change)
#greatest decrease in losses (date & amount) over the entire period
    min_avg_change=(avg_change)
    # date of min avg change
    date_min_avg_change=row(min_avg_change[row(0)])
        print("Greatest Decrease in Profits: ")
        print(date_min_avg_change)
        print(date_min_avg_change)
# Specify the file to write to
output_path = os.path.join("..", "output", "new.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['First Name', 'Last Name', 'SSN'])

    # Write the second row
    csvwriter.writerow(['Caleb', 'Frost', '505-80-2901']) """
