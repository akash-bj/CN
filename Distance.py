node = int(input("Enter the total number of nodes present: "))
dist = []
path = []

for i in range(node):
    dist.append([0] * node)
    path.append([None] * node)

print("Enter the cost matrix (use 0 for no direct path, and use a large number like 999 for infinity):")

for i in range(node):
    l = input().split()
    for j in range(node):
        dist[i][j] = int(l[j])
        if dist[i][j] != 0 and dist[i][j] != 999:
            path[i][j] = j
        elif i != j:
            dist[i][j] = 999

for k in range(node):
    for i in range(node):
        for j in range(node):
            if dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
                path[i][j] = path[i][k]

def get_path(i, j):
    if path[i][j] is None:
        return []
    route = [i]
    while i != j:
        i = path[i][j]
        route.append(i)
    return route

print("\nShortest Paths and Hubs:")

for i in range(node):
    for j in range(node):
        if i != j and dist[i][j] != 999:
            route = get_path(i, j)
            print(f"Shortest Path from {i} to {j}: {'->'.join(map(str, route))} with Distance {dist[i][j]}")
        elif i != j:
            print(f"No Path from {i} to {j}")
