import csv

def my_sign(x):
    return (x > 0) - (x < 0)

input_file = 'table2.csv'
output_file = 'table3.csv'

video_duration = 13.21
frame_count = 396

delta_t = video_duration / frame_count

lst = []

predicted = []

with open(input_file, mode='r') as infile:
    reader = csv.reader(infile)
    next(reader)
    for row in reader:
        lst.append((int(row[0]), float(row[1]), float(row[2]), float(row[3])))

with open("pendulum_.csv", mode='r') as infile:
    reader = csv.reader(infile)
    next(reader)
    for row in reader:
        predicted.append(float(row[2]))

nlst = []
for i in range(2,len(lst)-2):
    #Lagrange
    #L1 = (lst[i-2][1]/4 - 2*lst[i-1][1] + 2*lst[i+1][1] - lst[i+2][1]/4)/(3*delta_t)
    #L2 = (lst[i-2][2]/4 - 2*lst[i-1][2] + 2*lst[i+1][2] - lst[i+2][2]/4)/(3*delta_t)
    L = (lst[i-2][3]/4 - 2*lst[i-1][3] + 2*lst[i+1][3] - lst[i+2][3]/4)/(3*delta_t)
    nlst.append((lst[i][0],L,predicted[lst[i][0]]))

with open(output_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Frame", "Total Acceleration (cm/s^2)", "Predicted Acceleration (cm/s^2)"])
    writer.writerows(nlst)

