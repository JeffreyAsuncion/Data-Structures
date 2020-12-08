class Vertex:
    def __init__(self, value):
        self.value = value
        self.connections = {}

    def __str__(self):
        return str(self.value) + ' connections: ' + str([x.value for x in self.connections])

    def add_connection(self, vert, weight = 0):
        self.connections[vert] = weight

    def get_connection(self):
        return self.connections.keys()
    
    def get_value(self):
        return self.value
    
    def get_weight(self, vert):
        return self.connections[vert]


class Graph:
    def __init__(self):
        self.vertices = {}
        self.count = 0

    def __contains__(self, vert):
        return vert in self.vertices

    def __iter__(self):
        return iter(self.vertices.values())

    def add_vertex(self, value):
        self.count += 1
        new_vert = Vertex(value)
        self.vertices[value] = new_vert
        return new_vert

    def add_edge(self, v1, v2, weight = 0):
        if v1 not in self.vertices:
            self.add_vertex(v1)
        if v2 not in self.vertices:
            self.add_vertex(v2)
        self.vertices[v1].add_connection(self.vertices[v2], weight)
        
    
    def get_vertices(self):
        return self.vertices.keys()


g = Graph()
for i in range(8):
    g.add_vertex(i)

g.add_edge(0,1,3)
g.add_edge(0,7,2)
g.add_edge(1,3,4)
g.add_edge(2,2,1)
g.add_edge(3,6,5)
g.add_edge(4,0,2)
g.add_edge(5,2,3)
g.add_edge(5,3,1)
g.add_edge(6,2,3)
g.add_edge(7,1,4)

for v in g:
    print(v)
