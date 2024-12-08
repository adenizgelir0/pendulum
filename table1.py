import csv

input_file = 'locations.csv'
output_file = 'table1.csv'

con_rate = 41.88 / 550.8403

with open(input_file, mode='r') as infile:
    reader = csv.reader(infile)
    next(reader)
    with open(output_file, mode='w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["Frame", "X Position(cm)", "Y Position(cm)"])
        i=0
        for row in reader:
            writer.writerow([i,float(row[2])*con_rate, 82.11-float(row[3])*con_rate])
            i+=1

