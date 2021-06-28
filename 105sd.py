import math
import csv

with open('data1.csv',newline='')as f:
    reader=csv.reader(f)
    file_data=list(reader)
#mean
data=file_data[0]
def mean(data):
    n=len(data)
    total=0
    for x in data:
        total+= int(x)

    mean=total/n
    return mean
#square of the value
squared_list=[]
for number in data:
    a=int(number)-mean(data)
    a=a**2
    squared_list.append(a)
#getting sum
sum=0
for i in squared_list:
    sum=sum+i
#div the sum by total values
result=sum/(len(data)-1)
#std deviation formula
std_deviation=math.sqrt(result)
print(std_deviation)