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
#add edges between nodes
g.add_edge('c_1','peters_nw')
g.add_edge("c_1","c_2")
g.add_edge("c_1","c_17")
g.add_edge("c_1","c_18")

g.add_edge("c_2","peters_nw")
g.add_edge("c_2","c_3")

g.add_edge("c_3","peters_ne")
g.add_edge("c_3","c_4")

g.add_edge("c_4","artse_e")
g.add_edge("c_4","dh_w")
g.add_edge("c_4","c_5")

g.add_edge("c_5","music_ne")
g.add_edge("c_5","c_11")
g.add_edge("c_5","c_6")

g.add_edge("c_6","c_9")
g.add_edge("c_6","c_7")

g.add_edge("c_7","c_8")

g.add_edge("c_8","c_9")
g.add_edge("c_8","c_29")

g.add_edge("c_9","ac_s")
g.add_edge("c_9","c_10")

g.add_edge("c_10","c_11")
g.add_edge("c_10","c_31")

g.add_edge("c_11","c_12")
g.add_edge("c_11","c_33")

g.add_edge("c_12","music_sw")
g.add_edge("c_12","dh_s")
g.add_edge("c_12","frednichols_e")
g.add_edge("c_12","c_13")

g.add_edge("c_13","c_14")
g.add_edge("c_13","c_24")
g.add_edge("c_13","c_25")

g.add_edge("c_14","dawb_s")
g.add_edge("c_14","c_15")
g.add_edge("c_14","c_20")
g.add_edge("c_14","c_23")

g.add_edge("c_15","dawb_s")
g.add_edge("c_15","c_16")
g.add_edge("c_15","library_e")
g.add_edge("c_15","c_18")
g.add_edge("c_15","c_20")

g.add_edge("c_16","dawb_n")
g.add_edge("c_16","artsc_s")
g.add_edge("c_16","peters_se")
g.add_edge("c_16","schliegel_e")
g.add_edge("c_16","c_18")

g.add_edge("c_17","peters_sw")
g.add_edge("c_17","schliegel_nw")
g.add_edge("c_18","c_18")

g.add_edge("c_18","c_19")

g.add_edge("c_19","c_20")
g.add_edge("c_19","c_21")

g.add_edge("c_20","seminary_n")
g.add_edge("c_20","c_23")

g.add_edge("c_21","seminary_s")
g.add_edge("c_21","c_22")

g.add_edge("c_22","c_23")
g.add_edge("c_22","seminary_s")
g.add_edge("c_22","c_24")
g.add_edge("c_22","c_26")

g.add_edge("c_23","c_24")

g.add_edge("c_24","c_25")

g.add_edge("c_25","c_32")
g.add_edge("c_25","c_26")

g.add_edge("c_26","brickeracademic_s")
g.add_edge("c_26","c_27")

g.add_edge("c_27","science_sw")
g.add_edge("c_27","c_28")

g.add_edge("c_28","c_29")
g.add_edge("c_28","science_se")

g.add_edge("c_29","c_30")

g.add_edge("c_30","science_ne")
g.add_edge("c_30","c_31")

g.add_edge("c_31","c_32")
g.add_edge("c_31","science_nw")

g.add_edge("c_32","brickeracademic_n")
g.add_edge("c_32","c_33")

#FIX GET WEIGHT

#display output
for v in g:
    for w in v.get_connections():
        vid = v.get_id()
        wid = w.get_id()
        print ("( %s , %s, %.6f)"  % ( vid, wid, v.get_weight(w)))

for v in g:
    print ('g.vert_dict[%s]=%s' %(v.get_id(), g.vert_dict[v.get_id()]))