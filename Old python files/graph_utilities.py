'''
Loading the graph with values from the csv
'''
import csv
from graph import Graph
from graph import Vertex
import heapq
def load_graph(g):
    """
    Populate graph object with edges and vertices
    Parameters:
        g - graph object
    
    """
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
    g.add_edge("c_17","c_18")
    
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
    #adding inter building connections
    g.add_edge("peters_se","artsc_w")
    g.add_edge("artsc_e","artse_w")
    g.add_edge("dawb_s","frednichols_e")#this value is super sketchy since we couldnt get inside)
    #add edges between all doors in the same building
    #currently disabled so people dont walk through 100 buildings
    '''
    g.add_edge("laz_se","laz_n")
    g.add_edge("laz_se","laz_sw")
    g.add_edge("laz_n","laz_sw")  
    
    g.add_edge("music_ne","music_e")   
    g.add_edge("music_ne","music_sw")   
    g.add_edge("music_e","music_sw")         
    g.add_edge("dh_e","dh_s")
    g.add_edge("dh_e","dh_w")
    g.add_edge("dh_w","dh_s")
    
    g.add_edge("artse_e","artse_w")
    
    g.add_edge("artsc_e","artsc_n")
    g.add_edge("artsc_e","artsc_s")
    g.add_edge("artsc_e","artsc_w")
    g.add_edge("artsc_s","artsc_n")
    g.add_edge("artsc_w","artsc_n")
    g.add_edge("artsc_s","artsc_w")
    
    g.add_edge("peters_ne","peters_se")
    g.add_edge("peters_ne","peters_sw")
    g.add_edge("peters_ne","peters_nw")
    g.add_edge("peters_se","peters_nw")
    g.add_edge("peters_se","peters_sw")
    g.add_edge("peters_sw","peters_nw")
    
    g.add_edge("schliegel_e","schliegel_nw")
'''
def display_graph(g):
    '''
    Prints a visual representation of the graph by first printing all the edges
    and then printing all the nodes and listing the nodes adjacent to them
    ''' 
    #display all edges
    for v in g:
        for w in v.get_connections():
            vid = v.get_id()
            print ("( %s , %s, %.6f)"  % ( vid, w, v.get_weight(w)))
    #display all nodes and their adjacent nodes
    for v in g:
        print ('g.vert_dict[%s]=%s' %(v.get_id(), g.vert_dict[v.get_id()]))
    
def dijkstra(g,start, end):
    '''
    Calculates the shortest path from one node to another in a graph
    Does so by updating previous and distance values for each Vertex
    Parameters:
        g - the Graph object (Graph)
        start - the starting node (Vertex)
        end - the ending node (Vertex)
    '''
    #set the distance from the start node to zero
    start.set_distance(0)
    
    #put tuple pair into the heap
    unvisited_queue = [(v.get_distance(),v) for v in g]
    heapq.heapify(unvisited_queue)
    
    while len(unvisited_queue):
        #pops a vertex with the smallest distance
        uv = heapq.heappop(unvisited_queue)
        current = uv[1]
        current.set_visited()
        #go through each node adjacent to current
        for adj in current.adjacent:
            #skip if visited
            if g.vert_dict[adj].visited:
                continue
            #relax edges
            new_dist = current.get_distance() + current.get_weight(adj)
            if new_dist<g.vert_dict[adj].get_distance():
                g.vert_dict[adj].set_distance(new_dist)
                g.vert_dict[adj].set_previous(current)
            
        #rebuild heap
        #step 1 pop every item
        while len(unvisited_queue):
            heapq.heappop(unvisited_queue)
        #2 put all vertices not visited into the queue
        unvisited_queue = [(v.get_distance(),v)for v in g if not v.visited]
        heapq.heapify(unvisited_queue)
    
    
def shortest(v, path):
    ''' 
    Helper function called after Dijkstra's has been used
    goes through the graph and finds all the previous nodes in the path from v
    Parameters:
        v - the end node to trace back from (Vertex)
        path - the path of nodes in the shortest path (Array)
    '''
    if v.previous:
        path.append(v.previous.get_id()) #append the node to path if it has a previous value
        shortest(v.previous, path) #recall the function with the previous value
    return   
    
def get_closest_node_to_curr_location(g,latitude,longitude):
    '''
    Gets the closest node in the graph to the current location
    Parameters:
        latitude - current latitude
        longitude - current longitude
    Returns:
        closest - node in graph closest to current location
    '''
    curr_location = Vertex("curr_location",latitude,longitude)
    #get node with minimum distance
    vals = g.vert_dict.values()
    min_distance = 9999
    for v in vals:
        temp_distance = g.get_distance(curr_location,v)
        if(temp_distance<min_distance):
            min_distance = temp_distance
            min_node = v
            
    return min_node