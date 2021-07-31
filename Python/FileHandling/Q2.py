import csv
fileName = "sample.csv"
fields = []
rows = []
with open (fileName, 'r') as csvfile:
    csvReader = csv.reader(csvfile)
    fields = next(csvReader)

    for row in csvReader:
        rows.append(row)
        print(row)
csvfile.close()


'''Thought of a logic for writing a column using pandas pakage but it is not 
working on my device due to some package issue will try to think of another method till then'''
