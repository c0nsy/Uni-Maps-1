"""Graph Data Structure
Author: Max Dann
Email: maxkdann@hotmail.com
"""


class Vertex:

    def __init__(self, node,latitude,longitude):
        """
        Initialize a vertex object, no adjacent vertices at the beginning
        Neighbor nodes will be stored in the adjacent dictionary
        Parameters:
            node - node id (int)
            latitude - the latitude of the vertex (float)
            longitude - the longitude of the vertex (float)
        """
        self.id = node
        self.adjacent = {}
        self.latitude = latitude
        self.longitude = longitude
        
    def __str__(self):
        """
        To string function for readability and testing
        """
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])
    
    def add_neighbor(self, neighbor, weight=0):
        """
        Adds a neighbor to the vertex
        Parameters:
            neighbor - the node id of the adjacent vertex
            weight - the weight of the edge between the two nodes
        """
        self.adjacent[neighbor] = weight
    
    def get_connections(self):
        """
        Returns the connections of the node
        """
        return self.adjacent.keys()
    
    def get_id(self):
        """
        Returns the node id of the vertex
        """
        return self.id
    
    def get_weight(self, neighbor):
        """
        Returns the weight of the edge between the vertex and neighbor
        Parameters:
            neighbor - an adjacent vertex to the vertex
        Returns:
            weight - the weight of the edge connecting the two vertices
        """
        return self.adjacent[neighbor]

    
class Graph:

    def __init__(self):
        """
        Initialize a graph object, use a dictionary to store vertices
        initially the graph has no vertices
        """
        self.vert_dict = {}
        self.num_vertices = 0
        
    def __iter__(self):
        """
        iter method to allow for a loop to iterate through vertices in the graph
        """
        return iter(self.vert_dict.values())
    
    def add_vertex(self, node):
        """
        Adds a vertex to the graph, updates vertex count and adds vertex to the graph dictionary
        Parameters:
            node - node id of vertex to add
        Returns:
            new_vertex = a new vertex object
        """
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex
        
    def get_vertex(self, n):
        """
        Returns a specified vertex in the graph
        Parameters:
            n - node id of vertex requested
        Returns:
            if node is in graph then return the node, else none
        """
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None
        
    def add_edge(self, frm, to, cost=0):
        """
        Adds an edge to the graph
        Parameters:
            frm - the from vertex
            to - the to vertex
            cost - the weight of the edge between the from and to vertices
        """
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)
        
        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)
        
    def get_vertices(self):
        """
        Returns all the vertices in the graph
        """
        return self.vert_dict.keys()
    
    
