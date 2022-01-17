class Graph:
    def __init__(self, node):
        self.visited = [None] * len(node)
        self.node = node
        self.adjacency_list = {}
        self.list1 = []
        for vertex in node:
            self.adjacency_list[vertex] = []

    def add_node(self, node, value):
        self.adjacency_list[node].append(value)

    def print_graph(self):
        for node in self.node:
            print(node, ":", self.adjacency_list[node])

    def detectCycle(self, starting_node):
        self.list1.append(starting_node)
        self.visited[starting_node] = 0
        while len(self.list1) > 0:
            for value in self.adjacency_list[self.list1[0]]:
                if self.visited[value] == 1:
                    return True
                if self.visited[value] == None:
                    self.list1.append(value)
                    self.visited[value] = 0
            self.visited[self.list1.pop(0)] = 1
        return False


node = [0, 1, 2, 3, 4, 5, 6]
graph = Graph(node)
edges = [(0, 1), (0, 2), (1, 3), (1, 5), (6, 5), (3, 2), (2, 4)]
for (e, v) in edges:
    graph.add_node(e, v)
graph.print_graph()
print(graph.detectCycle(0))
