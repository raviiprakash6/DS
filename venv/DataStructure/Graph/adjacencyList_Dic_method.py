class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.adjacency_list = {}
        for node in self.nodes:
            self.adjacency_list[node] = []

    def add_node(self,node,value):
        self.adjacency_list[node].append(value)
        self.adjacency_list[value].append(node)


    def print_graph(self):
        for node in self.nodes:
            print(node, ":", self.adjacency_list[node])


node = [1, 2, 3, 5]
graph = Graph(node)
edges = [(1, 2), (1, 3), (1, 5), (2, 5), (3, 5)]
for (e, v) in edges:
    graph.add_node(e, v)
graph.print_graph()
