import matplotlib.pyplot as plt
import csv

x=[]
y=[]

with open('emp.csv','r') as fo:
#of = open('emp.csv','r')
    data = csv.reader(fo,delimiter=',')
    for row in data:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.plot(x,y)

plt.title("Load data from file")

plt.show()
