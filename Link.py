def find_all_paths(graph, start, end, path=None):
    if path is None:
        path = [start]

    if start == end:
        return [path]

    paths = []
    for node in range(len(graph)):
        if graph[start][node] not in (0, 999) and node not in path:
            for new_path in find_all_paths(graph, node, end, path + [node]):
                paths.append(new_path)
    return paths

def find_shortest_path(graph, start, end):
    all_paths = find_all_paths(graph, start, end)

    if not all_paths:
        return None, float('inf')

    shortest_path = min(
        all_paths,
        key=lambda path: sum(graph[path[i]][path[i+1]] for i in range(len(path) - 1))
    )

    shortest_distance = sum(
        graph[shortest_path[i]][shortest_path[i+1]]
        for i in range(len(shortest_path) - 1)
    )

    return shortest_path, shortest_distance

graph = [list(map(int, input().split()))
         for _ in range(int(input("Enter the total number of nodes present: ")))]

for src in range(len(graph)):
    for dest in range(len(graph)):
        if src != dest:
            paths = find_all_paths(graph, src, dest)

            if paths:
                print(f"All Paths from {src} to {dest}:")
                for path in paths:
                    distance = sum(graph[path[i]][path[i+1]] for i in range(len(path) - 1))
                    print(f"{' -> '.join(map(str, path))} with Distance {distance}")

                shortest_path, shortest_distance = find_shortest_path(graph, src, dest)
                print(f"Shortest Path from {src} to {dest}: {' -> '.join(map(str, shortest_path))} with Distance {shortest_distance}\n")
            else:
                print(f"No Path from {src} to {dest}\n")
