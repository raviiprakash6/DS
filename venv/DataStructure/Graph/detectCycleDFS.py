import sys


class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.adjacency_list = {}
        self.set1 = set()
        self.previous_parent = None
        for node in self.nodes:
            self.adjacency_list[node] = []

    def add_node(self, node, value):
        self.adjacency_list[node].append(value)
        self.adjacency_list[value].append(node)

    def recursive(self, key, parent):
        for value in self.adjacency_list[key]:
            if value in self.set1 and value != parent:
                print("True")
                exit()
            elif value not in self.set1:
                self.set1.add(value)
                self.recursive(value, key)

    def detectCycle(self):
        for key in self.adjacency_list.keys():
            if key not in self.set1:
                self.previous_parent = key
                self.set1.add(key)
                self.recursive(key, self.previous_parent)

    def print_graph(self):
        for node in self.nodes:
            print(node, ":", self.adjacency_list[node])


node = [0, 1, 2, 3]
graph = Graph(node)
edges = [(0, 1), (1, 2), (1, 3),(2,3)]
for (e, v) in edges:
    graph.add_node(e, v)
graph.print_graph()
graph.detectCycle()
