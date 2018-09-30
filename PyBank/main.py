# Read data from budget_data.csv
import os
import csv
import datetime
csvpath = os.path.join('budget_data.csv')

#Initialize variables
countRow = 0
totalNetAmount = 0
# Declare change amount array
changeAmt = [0.0]
#currentMonth = [""]
averageChange = 0.0
totalChange = 0.0
gIAmt = 0.0
gIRow = 0
gDAmt = 0.0
gDRow = 0
gIMonth = ""
gDMonth = ""
#Reading using CSV module
with open(csvpath, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first 
    csv_header = next(csvreader)
    previousAmount = 0
    # Read each row of data after the header
    # Loop each row in the csv file
    for row in csvreader:
        # Increment count 
        countRow += 1
        # Store current amount as variable and current Month as array
        currentAmount = int(row[1])
        #currentMonth.append(row[0])
        # This is sum of all amounts including first one
        totalNetAmount += currentAmount
        # Calculate change amount in loop, this will be 0 for 1st row as initialized
        change = currentAmount - previousAmount
        #totalChange += change
        # After first row, run if condition
        if(countRow > 1):
            # Store change in an array
            changeAmt.append(change)
            if(change > gIAmt):
                gIMonth = row[0]
                #gIMonth = datetime.date(row[0])
                #print("GI MOnth" + str(gIMonth))
                gIAmt = change
            if(change < gDAmt):
                gDMonth = row[0]
                gDAmt = change
        # store previous amount value here before the for loop goes to next row                
        previousAmount = currentAmount

# Initialize row counter for the Change amount array
changesRow = 1
for x in changeAmt:
    # This loop should run from 2nd row to last row and is to calculate total change
    totalChange += x

# Calculate Average change from total change
averageChange = totalChange / (countRow-1)

# Convert Months to format eg. Feb-12 to Feb-2012
# Steps are to breakdown current format to temp variable, and then put back changing year from 2 to 4 digit
dt = datetime.datetime.strptime(gIMonth,'%b-%y')
gIMonth = datetime.datetime.strftime(dt,'%b-%Y')
dt2 = datetime.datetime.strptime(gDMonth,'%b-%y')
gDMonth = datetime.datetime.strftime(dt2,'%b-%Y')

#Print Output
print(f'''Financial Analysis
----------------------------''')
print(f"Total months: {countRow}")
print(f"Total: ${totalNetAmount}")
print(f"Average change: ${round(averageChange,2)}")
print(f'Greatest Increase in Profits: {gIMonth} (${gIAmt})')
print(f'Greatest Decrease in Profits: {gDMonth} (${gDAmt})')

