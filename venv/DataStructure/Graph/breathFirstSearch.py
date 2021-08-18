class Graph:
    def __init__(self, node):
        self.set1 = set()
        self.node = node
        self.adjacency_list = {}
        self.list1 = []
        for vertex in node:
            self.adjacency_list[vertex] = []

    def add_node(self, node, value):
        self.adjacency_list[node].append(value)
        self.adjacency_list[value].append(node)

    def print_graph(self):
        for node in self.node:
            print(node, ":", self.adjacency_list[node])

    def print_BFS(self, starting_node):
        self.list1.append(starting_node)
        self.set1.add(starting_node)
        while len(self.list1) > 0:

            for i in self.adjacency_list[self.list1[0]]:
                if i not in self.set1:
                    self.set1.add(i)
                    self.list1.append(i)

            print(self.list1[0])
            self.list1.pop(0)
    # for node in self.node:
    #
    # pass


node = [1, 2, 3, 5 , 8, 7, 6]
graph = Graph(node)
edges = [(1, 2), (1, 3), (1, 5), (2, 5), (3, 5), (3, 6), (2, 7), (7, 8)]
for (e, v) in edges:
    graph.add_node(e, v)
graph.print_graph()
graph.print_BFS(5)
