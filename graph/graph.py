from collections import defaultdict

class Graph:
    def __init__(self, directed=False):
        self.graph = defaultdict(list)
        self.directed = directed

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, u, v, weight=1): 
        self.graph[u].append((v, weight))  
        if not self.directed:
            self.graph[v].append((u, weight)) 

    def __getitem__(self, node):
        return self.graph[node]

    def __str__(self):
        return "\n".join(f"{node}: {neighbors}" for node, neighbors in self.graph.items())