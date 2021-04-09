"""
testing the graph
"""
from graph import Graph

g = Graph()

g.add_vertex('a',10,10)
g.add_vertex('b',20,20)
g.add_vertex('c',30,30)

g.add_edge('a', 'b')  
g.add_edge('a', 'c')
g.add_edge('b', 'c')


for v in g:
    for w in v.get_connections():
        vid = v.get_id()
        wid = w.get_id()
        print ("( %s , %s, %3d)"  % ( vid, wid, v.get_weight(w)))

for v in g:
    print ('g.vert_dict[%s]=%s' %(v.get_id(), g.vert_dict[v.get_id()]))