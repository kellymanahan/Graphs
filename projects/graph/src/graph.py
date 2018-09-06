"""
Simple graph implementation compatible with BokehGraph class.
"""
# class Vertex:
#     def __init__(self, label):
#         self.label = label
#         self.edges = set()

#     def __repr__(self):
#         return 'Vertex' + self.label
class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
       self.vertices = {}
    
    def add_vertex(self, vertex):
        if vertex in self.vertices:
            raise ValueError('there is already a vertex')
        else:
            self.vertices[vertex] = set()

    def add_edge(self, start, end):
        if start not in self.vertices or end not in self.vertices:
            return False
        else:
            self.vertices[start].add(end)
            return True


    