'''
Main module
'''
from graph_utilities import load_graph
from graph import Graph
from graph_utilities import dijkstra
from graph_utilities import shortest
from graph_utilities import display_graph
from graph_utilities import get_closest_node_to_curr_location


def main():
    # replace this with whatever your start node is
    #start = "dawb_n"
    # start_lat = input("Input your starting latitude: ")
    # start_long = input("Input your starting longitude: ")
    #replace these values with your starting location (from front end)
    start_lat = 43.47359
    start_long = -80.525
    
    # replace this with whatever your end node is (from front end)
    end = "science_se"
    # make a graph object
    g = Graph()
    # load all graph nodes and edges
    load_graph(g)
    # display the graph if you want to see a visual representation
    display_graph(g)
    #get the node already in the graph closest to your current location
    start = get_closest_node_to_curr_location(g,start_lat,start_long)
    # compute shortest path
    dijkstra(g, g.get_vertex(start.id), g.get_vertex(end))
    target = g.get_vertex(end)
    path = [target.get_id()]  # gets the path to stop at the end vertex
    shortest(target, path)
    # display the path, notice it prints in reverse
    print('Shortest path: %s' % path[::-1])


main()

