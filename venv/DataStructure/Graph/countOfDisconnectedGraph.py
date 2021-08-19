class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.set1 = set()
        self.list = []
        self.count = 0
        self.adjacency_list = {}
        for node in self.nodes:
            self.adjacency_list[node] = []

    def add_node(self, node, value):
        self.adjacency_list[node].append(value)
        self.adjacency_list[value].append(node)

    def countOfDisconnectedGraph(self):
        for key in self.adjacency_list.keys():
            if key not in self.set1:
                self.count += 1
                self.set1.add(key)
                self.list.append(key)
            for value in self.adjacency_list[key]:
                if value not in self.set1:
                    self.set1.add(value)
                    self.list.append(value)
                    self.list.pop(0)
        return print(self.count)

    def print_graph(self):
        for node in self.nodes:
            print(node, ":", self.adjacency_list[node])


node = [0, 1, 2, 3, 4, 5, 6, 7, 8]
graph = Graph(node)
edges = [(0, 1), (0, 2), (1, 3), (2, 3), (4, 5), (4, 6), (5, 6), (7, 8)]
for (e, v) in edges:
    graph.add_node(e, v)
graph.print_graph()
graph.countOfDisconnectedGraph()
