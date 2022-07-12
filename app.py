import csv
from matplotlib.colors import hex2color
import pandas as pd

file_1 = 'data.csv'
file_2 = 'data(128).csv'

data_1 = []
data_2 = []

with open(file_1, 'r') as f:
    csv_reader = csv.reader(f)

    for i in csv_reader:
        data_1.append(i)

with open(file_2, 'r') as f:
    csv_reader = csv.reader(f)

    for i in csv_reader:
        data_2.append(i)

header1 = data_1[0]
header2 = data_2[0]

h = header1+header2

with open('Data_merged.csv','w') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(h)   

df = pd.read_csv('Data_merged.csv')

df.tail(8)
print('files are merged')