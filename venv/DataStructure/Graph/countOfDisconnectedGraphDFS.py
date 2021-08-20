class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.set1 = set()
        self.count = 0
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
                # print("value:", value)
                self.printDepthKey(value)

    def countOfDisconnectedGraph(self):
        for key in self.adjacency_list.keys():
            if key not in self.set1:
                self.set1.add(key)
                self.count += 1
                # print("key:", key)
                self.printDepthKey(key)
        print("count of disconnected graph is", self.count)

    def print_graph(self):
        for node in self.nodes:
            print(node, ":", self.adjacency_list[node])


node = [0, 1, 2, 3, 4, 5, 7, 8]
graph = Graph(node)
edges = [(0, 1), (0, 2), (2, 3), (1, 4), (4, 5), (7, 8)]
for (e, v) in edges:
    graph.add_node(e, v)
graph.print_graph()
graph.countOfDisconnectedGraph()
