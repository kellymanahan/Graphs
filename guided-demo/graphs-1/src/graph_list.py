"""Graph representation using adjacency list."""

class Edge:
    """Edges in the adjacency list are just a destination."""
    # Using simple classes for illustrative purposes
    # pylint: disable=too-few-public-methods
    def __init__(self, destination):
        self.destination = destination


class Vertex:
    """Vertices have a label and a set of edges."""
    # pylint: disable=too-few-public-methods
    def __init__(self, label):
        self.label = label
        self.edges = set()

    def __repr__(self):
        return str(self.label)


class Graph:
    """The graph itself is simply a set of vertices."""
    # pylint: disable=too-few-public-methods
    def __init__(self):
        self.vertices = set()

    def add_edge(self, start, end):
        start.edges.add(end)

    def add_vertex(self, vertex):
        self.vertex.add(vertex)
