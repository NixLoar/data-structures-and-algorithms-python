def DFS(graph, start):
    visited = set()
    result = []

    def rec(node):
        if node not in visited:
            visited.add(node)
            result.append(node)
            for neighbor in graph[node]:
                rec(neighbor)

    rec(start)
    return result