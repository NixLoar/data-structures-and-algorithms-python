def Toposort(graph):
    in_degree = {node: 0 for node in graph.graph}

    for node in graph.graph:
        for neighbor, _ in graph.graph[node]: 
            in_degree[neighbor] += 1

    queue = [node for node in in_degree if in_degree[node] == 0]
    top_order = []

    while queue:
        current_node = queue.pop(0) 
        top_order.append(current_node)

        for neighbor, _ in graph.graph[current_node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(top_order) != len(graph.graph):
        return("Error! Graph has cycles")

    return top_order