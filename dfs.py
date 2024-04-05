def dfs(graph, start, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(start)
    path.append(start)

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited, path)

    return path

# Граф в виде словаря смежности
graph = {
    1: [3],
    2: [4],
    3: [],
    4: [2]
}

# Стартовая вершина
start_vertex = 1

# Получение пути обхода
result_path = dfs(graph, start_vertex)

if result_path:
    print("Путь:", result_path)
else:
    print("Путь от вершины {} до вершины {} не найден.".format(vertex_a, vertex_b))
