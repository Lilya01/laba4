#добавил коментарии
def dfs(graph, start, end, visited=None, path=None):
    #12321312312312
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(start)
    path.append(start)

    if start == end:
        return path, len(path) - 1

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            result_path, path_length = dfs(graph, neighbor, end, visited, path)
            if result_path:
                return result_path, path_length

    path.pop()
    visited.remove(start)

    return None, 0

# Граф в виде словаря смежности
graph = {
    1: [3],
    2: [4],
    3: [],
    4: [2]
}

# Входные параметры - вершины a и b
vertex_a = 2
vertex_b = 4

if vertex_a not in graph or vertex_b not in graph:
    print("Вершины {} или {} отсутствуют в графе.".format(vertex_a, vertex_b))
else:
    # Получение пути обхода и длины пути от вершины a до вершины b
    result_path, path_length = dfs(graph, vertex_a, vertex_b)

    if result_path:
        print("Путь:", result_path)
        print("Длина пути от вершины {} до вершины {}: {}".format(vertex_a, vertex_b, path_length))
    else:
        print("Путь от вершины {} до вершины {} не найден.".format(vertex_a, vertex_b))
