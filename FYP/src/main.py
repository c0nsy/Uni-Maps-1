'''
Main module
'''
from graph_utilities import load_graph
from graph import Graph
from graph_utilities import dijkstra
from graph_utilities import shortest
from graph_utilities import display_graph
def main():
    #start = input("Input current location:");
    #end = input("Input destination:")
    start = "c_1"
    end = "c_9"
    g = Graph()
    load_graph(g)
    display_graph(g)
    dijkstra(g,g.get_vertex(start),g.get_vertex(end))
    target = g.get_vertex(end)
    path = [target.get_id()]
    shortest(target,path)
    print("Shortest path: %s",path[::-1])
main()