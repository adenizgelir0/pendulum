import csv

def my_sign(x):
    return (x > 0) - (x < 0)


input_file = 'table1.csv'
output_file = 'table2.csv'

video_duration = 13.21
frame_count = 396

delta_t = video_duration / frame_count

lst = []

predicted = []

with open(input_file, mode='r') as infile:
    reader = csv.reader(infile)
    next(reader)
    for row in reader:
        lst.append((int(row[0]), float(row[1]), float(row[2])))

with open("pendulum_.csv", mode='r') as infile:
    reader = csv.reader(infile)
    next(reader)
    for row in reader:
        predicted.append(float(row[3]))


nlst = []
for i in range(2,len(lst)-2):
    #Lagrange
    L1 = (lst[i-2][1]/4 - 2*lst[i-1][1] + 2*lst[i+1][1] - lst[i+2][1]/4)/(3*delta_t)
    L2 = (lst[i-2][2]/4 - 2*lst[i-1][2] + 2*lst[i+1][2] - lst[i+2][2]/4)/(3*delta_t)
    nlst.append((lst[i][0],L1,L2,my_sign(L1)*(L1*L1 + L2*L2)**0.5,predicted[i]))

with open(output_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Frame", "X Velocity(cm/s)", "Y Velocity(cm/s)",
                     "Total Velocity(cm/s)", "Predicted Velocity(cm/s)"])
    writer.writerows(nlst)

