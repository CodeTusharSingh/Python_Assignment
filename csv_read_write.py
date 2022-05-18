import csv
with open('Book1.csv','r') as f:
    csvreader = csv.reader(f)
    header = []
    header = next(csvreader)
    print(header)
    rows = []
    for row in csvreader:
        rows.append(row)
    print(rows)
    for i in rows:
        print("Rows",i)
    f.close()
with open('Book1.csv', 'r') as f:
    f1 = csv.DictReader(f)
    a1 = []
    a2 = []
    a3 = []
    a4 = []
    for j in f1:
        a1.append(j['a1'])
        a2.append(j['a2'])
        a3.append(j['a3'])
        a4.append(j['a4'])
    print("a1", a1)
    print("a2", a2)
    print("a3", a3)
    print("a4", a4)
    f.close()
sum1 = 0
for i in a1:
    i = float(i)
    sum1 += i
avg1 = sum1/len(a1)
print("Mean of a1", avg1)
sum2 = 0
for i in a2:
    i = float(i)
    sum2 += i
avg2 = sum2/len(a2)
print("Mean of a2", avg2)
sum3 = 0
for i in a3:
    i = float(i)
    sum3 += i
avg3 = sum3/len(a3)
print("Mean of a3", avg3)
sum4 = 0
for i in a4:
    i = float(i)
    sum4 += i
avg4 = sum4/len(a4)
print("Mean of a4", avg4)
# with open('Book1.csv','a') as f:
#     writer_object = csv.writer(f)
#     mean = [avg1, avg2, avg3, avg4]
#     writer_object.writerow(mean)
#     f.close()
