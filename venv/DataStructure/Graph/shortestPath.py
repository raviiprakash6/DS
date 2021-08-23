class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.adjacency_list = {}
        self.set1 = set()
        self.list1 = []
        self.distance = [None] * len(self.nodes)
        for node in self.nodes:
            self.adjacency_list[node] = []

    def add_node(self, node, value):
        self.adjacency_list[node].append(value)
        self.adjacency_list[value].append(node)

    def shortestPath(self, start):
        self.set1.add(start)
        self.list1.append(start)
        self.distance[start] = 0
        print(start, ":", self.distance[start])
        while len(self.list1) > 0:
            for value in self.adjacency_list[self.list1[0]]:
                if value not in self.set1:
                    self.distance[value] = self.distance[self.list1[0]] + 1
                    print(value, ":", self.distance[value])
                    self.set1.add(value)
                    self.list1.append(value)
            self.list1.pop(0)

    def print_graph(self):
        for node in self.nodes:
            print(node, ":", self.adjacency_list[node])


node = [0, 1, 2, 3, 4, 5, 6]
graph = Graph(node)
edges = [(0, 1), (0, 2), (0, 3), (2, 3), (2, 4), (1, 3), (1, 5), (5, 6)]
for (e, v) in edges:
    graph.add_node(e, v)
graph.print_graph()
graph.shortestPath(0)
