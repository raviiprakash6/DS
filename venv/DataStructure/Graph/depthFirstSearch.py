class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.set1 = set()
        self.list = []
        self.adjacency_list = {}
        for node in self.nodes:
            self.adjacency_list[node] = []

    def add_node(self, node, value):
        self.adjacency_list[node].append(value)
        self.adjacency_list[value].append(node)

    def printDepthKey(self, key):
        for value in self.adjacency_list[key]:
            if value not in self.set1:
                self.set1.add(value)
                print(value)
                return self.printDepthKey(value)

    def depthFirstSearch(self):
        for key in self.adjacency_list.keys():
            if key not in self.set1:
                self.set1.add(key)
                print(key)
                self.printDepthKey(key)

    def print_graph(self):
        for node in self.nodes:
            print(node, ":", self.adjacency_list[node])


node = [0, 1, 2, 3, 4, 5]
graph = Graph(node)
edges = [(0, 1), (0, 2), (2, 3), (1, 4), (4, 5)]
for (e, v) in edges:
    graph.add_node(e, v)
graph.print_graph()
graph.depthFirstSearch()
