class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.adjacency_list = {}
        self.set1 = set()
        self.list = []
        for node in self.nodes:
            self.adjacency_list[node] = []

    def add_node(self, node, value):
        self.adjacency_list[node].append(value)
        self.adjacency_list[value].append(node)

    def print_graph(self):
        for node in self.nodes:
            print(node, ":", self.adjacency_list[node])

    def print_bfs_disconnected_graph(self):
        for key in self.adjacency_list.keys():
            if key not in self.set1:
                self.set1.add(key)
                self.list.append(key)
            for value in self.adjacency_list[key]:
                if value not in self.set1:
                    self.set1.add(value)
                    self.list.append(value)
            print(self.list.pop(0))


node = [0, 1, 2, 3, 5, 4, 6]
graph = Graph(node)
edges = [(0, 1), (0, 2), (1, 3), (2, 3), (4, 5), (4, 6), (5, 6)]
for (e, v) in edges:
    graph.add_node(e, v)
graph.print_graph()
graph.print_bfs_disconnected_graph()
