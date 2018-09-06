#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""

from sys import argv
from graph import Graph
import random

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
    nodes = [] 
    colors = {}
    my_que = collections.deque()
    for key in graph.vertices.keys():
        colors[key] = "white"

    my_queue.qppend(str(start_vert))
    colors[start_vert] = "grey"

    while len(my_queue) != 0:
        node = my_queue[0]
        neighbors = graph.vertices[node]
        for n in neighbors:
            if colors[n] =="white":
                my_queue.append(str(n))
                colors[n] = "grey"
        colors[node] = "black"
        nodes.append(my_queue.popleft())

        return nodes
        
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


def main():
    graph = Graph()
    # graph = draw_random_graph(graph, 5, 10)
    # graph.add_vertex(3)
    graph.add_edge(0,7)
    print_graph(graph)

if __name__ == '__main__':
    # TODO - parse argv
    main()
