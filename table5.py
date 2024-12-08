import csv
import math

input_file = 'table3.csv'
output_file = 'table5.csv'


lst = []

with open(input_file, mode='r') as infile:
    reader = csv.reader(infile)
    next(reader)
    for row in reader:
        lst.append((float(row[0]),float(row[1]), float(row[2])))

nlst = []
for e in lst:
    nlst.append((e[0],e[1],e[2],math.fabs(e[1]-e[2])))

with open(output_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Frame","Total Acceleration (cm/s^2)",
     "Predicted Acceleration (cm/s^2)", "Error(cm/s^2)"])
    writer.writerows(nlst)

