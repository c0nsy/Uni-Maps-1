'''
Loading the graph with values from the csv
'''
import csv
from graph import Graph

g = Graph()

with open('Node Values.csv','r',encoding="utf-8-sig") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[0])