class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.adjacency_list = {}
        self.list1 = [None] * len(nodes)
        self.set1 = set()
        for node in self.nodes:
            self.adjacency_list[node] = []

    def add_node(self, node, value):
        self.adjacency_list[node].append(value)

    def isCycle(self, key):
        for value in self.adjacency_list[key]:
            if value not in self.set1:
                self.set1.add(value)
                self.list1[value] = True
                self.isCycle(value)
            elif value in self.set1 and self.list1[value] == True:
                print("True")
                exit()
            self.list1[value] = False

    def detectCycle(self):
        for key in self.adjacency_list.keys():
            if key not in self.set1:
                self.set1.add(key)
                self.list1[key] = True
                self.isCycle(key)
                self.list1[key] = False

    def print_graph(self):
        for node in self.nodes:
            print(node, ":", self.adjacency_list[node])


node = [0, 1, 2, 3, 4, 5]
graph = Graph(node)
edges = [(0, 1), (2, 1), (2, 3), (3, 4), (4, 5), (5, 3)]
for (e, v) in edges:
    graph.add_node(e, v)
graph.print_graph()
graph.detectCycle()
