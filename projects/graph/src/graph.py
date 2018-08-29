"""
Simple graph implementation compatible with BokehGraph class.
"""
class Vertex:
    def __init__(self, label):
        self.label = label
        self.edges = set()

    def __repr__(self):
        return str(self.label)

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.verticies = {}

    def add_edge(self, start, end):
        if start not in self.verticies and end not in self.verticies:
            raise ValueError("No valid entries")
        else:
            self.verticies[start].add(end)
            self.verticies[end].add(start)

    def add_vertex(self, vertex):
        if vertex not in self.verticies:
            self.verticies[vertex] = set()
        else:
            raise ValueError("Already in the set")




graph = Graph()
v1 = Vertex('V1')
graph.add_vertex(v1)
v2 = Vertex('V2')
graph.add_vertex(v2)
v3 = Vertex('V3')
graph.add_vertex(v3)
# graph.add_edge('3', '4')
graph.add_edge(v1, v2)
graph.add_edge(v1, v3)
print(graph.verticies)

