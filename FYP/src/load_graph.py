'''
Loading the graph with values from the csv
'''
import csv
from graph import Graph

g = Graph()
#add nodes from csv to graph
with open('Node Values.csv','r',encoding="utf-8-sig") as file:
    reader = csv.reader(file)
    for row in reader:
        g.add_vertex(row[0],row[1],row[2])

for v in g:
    for w in v.get_connections():
        vid = v.get_id()
        wid = w.get_id()
        print ("( %s , %s, %3d)"  % ( vid, wid, v.get_weight(w)))

for v in g:
    print ('g.vert_dict[%s]=%s' %(v.get_id(), g.vert_dict[v.get_id()]))