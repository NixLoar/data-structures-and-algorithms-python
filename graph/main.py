from graph import Graph
from dfs import DFS
from bfs import BFS
from dijkstra import Dijkstra
from topo_sort import Toposort

# Example on how to use it
graph = Graph(directed=False)

graph.add_edge("A", "B", 1) 
graph.add_edge("A", "C", 2)
graph.add_edge("B", "D", 3)
graph.add_edge("C", "D", 1)
graph.add_edge("D", "E", 4)

print("Graph:")
print(graph)

print("\nBFS starting from 'A':", BFS(graph, "A")) 
print("DFS starting from 'A':", DFS(graph, "A")) 

print("\nDijkstra's shortest path from 'A':", Dijkstra(graph, "A"))

print("\nTopological Sort:", Toposort(graph))