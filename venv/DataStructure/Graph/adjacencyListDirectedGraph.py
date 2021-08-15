class Graph:
    def __init__(self):
        # self.node = node
        self.adjacency_list = {}

    def add_nodes(self, vertex, edge):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
        self.adjacency_list[vertex].append(edge)

    def print_graph(self):
        for node in self.adjacency_list.keys():
            print(node, ":", self.adjacency_list[node])


graph = Graph()
edges = [(1, 2), (2, 1), (3, 1), (2, 3), (1,4)]
for (e, v) in edges:
    graph.add_nodes(e, v)
graph.print_graph()
