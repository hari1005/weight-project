import csv
with open("SOCR-HeightWeight.csv") as h:
    reader=csv.reader(h)
    file_data = list(reader)

file_data.pop(0)

new_data=[]
for i in range(len(file_data)):
    n_num=file_data[i][1]
    new_data.append(float(n_num))

n=len(new_data)
total=0
for x in new_data:
    total += x

mean=total/n
print("mean is" + str(mean))

if n % 2==0:
    meadian1=float(new_data(n//2))
    meadian2=float(new_data(n//2 -1))
    meadian=(meadian1+meadian2)/2
else:
    meadian=new_data(n//2)
    print(n)
print("meadian:"+str(meadian)) 