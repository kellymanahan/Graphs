#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""

from sys import argv
from graph import Graph
import random
import collections

#solution code
def draw_random_graph(graph, vertices, edges):
    for i in range(vertices):
        graph.add_vertex(str(i))
        j = 0
        while j <= edges: 
    
            success = graph.add_edge(str(random.randint(0, vertices-1)),str(random.randint(0, vertices-1)))
            if success:
                j += 1
    return graph

def print_graph(graph):
    for v in graph.vertices:
        line = ""
        line += (str(v) + ": " )
        for e in graph.vertices[v]:
            line += str( e ) + " "
        print( line )
#solution code
def bfs(graph, start_vert):
    visited= []
    #nodes = [] 
    colors = {}
    my_queue = collections.deque()
    for key in graph.vertices.keys():
        colors[key] = "white"

    my_queue.append(start_vert)
    colors[start_vert] = "grey"

    while len(my_queue) != 0:
        node = my_queue[0]
        neighbors = graph.vertices[node]
        if node not in visited:#added this
            visited.append(node) #added this
        for n in neighbors:
            if n not in visited: #added this
                colors[n] =="white"
                my_queue.append(n)
                colors[n] = "grey"
        colors[node] = "black"
        visited.append(my_queue.popleft()) #changed visited to nodes

        return visited #changed from nodes
        
def dfs(graph):
    nodes = [] 
    colors = {}
    my_que = collections.deque()
    for key in graph.vertices.keys():
        colors[key] = "white"
    def DFS_visit(v):
        colors[v] = "grey"
        nodes.append(v)
        for n in graph.vertices[str(v)]:
            if colors[n] =="white":
                nodes.append(n)
            DFS_visit(n)
        colors[v] = "black"

    return nodes

def connected_comps(graph): #_get_random_colors
    connected_components = []
    visited = set()
    #loop to find the vertices
    for vertex in graph.vertices.keys():
        #set to a color
        if vertex not in visited:#0(1)
            #include getrandomcolors
            # use BFS
            comp = bfs(graph, vertex)
            #save returned component to list of all components
            connected_components.append(comp)#[1,3,4]
            for c in comp:
                visited.update(comp)
                print("Hey:", c)
    return connected_components 

def main():
    graph = Graph()
    #graph = draw_random_graph(graph, 5, 10)
    graph.add_vertex(3)
    graph.add_vertex(6)
    graph.add_vertex(4)
    graph.add_edge(3,4)
    #print(graph)
    print("here it is: ", connected_comps(graph))
    # print_graph(graph)

if __name__ == '__main__':
    # TODO - parse argv
    main()

