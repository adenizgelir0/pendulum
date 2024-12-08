import csv
import math

input_file = 'table2.csv'
output_file = 'table4.csv'


lst = []

with open(input_file, mode='r') as infile:
    reader = csv.reader(infile)
    next(reader)
    for row in reader:
        lst.append((float(row[0]),float(row[3]), float(row[4])))

nlst = []
for e in lst:
    nlst.append((e[0],e[1],e[2],math.fabs(e[1]-e[2])))

with open(output_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Frame","Total Velocity (cm/s)", "Predicted Velocity (cm/s)", "Error(cm/s)"])
    writer.writerows(nlst)

