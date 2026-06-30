from collections import deque
import heapq

# ---------------- GRAPH ----------------
graph = {
    "A": {"B":2, "C":4},
    "B": {"D":3, "E":5},
    "C": {"F":2},
    "D": {"G":4},
    "E": {"G":2, "H":3},
    "F": {"H":4},
    "G": {"I":2},
    "H": {"J":3},
    "I": {"J":2},
    "J": {}
}

heuristic = {
    "A":10,
    "B":8,
    "C":7,
    "D":6,
    "E":5,
    "F":5,
    "G":3,
    "H":2,
    "I":1,
    "J":0
}

# ---------------- BFS ----------------
def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    visited = set()
    explored = 0

    while queue:
        node, path = queue.popleft()
        explored += 1

        if node == goal:
            return path, "N/A", explored

        if node not in visited:
            visited.add(node)

            for neighbor in graph[node]:
                queue.append((neighbor, path + [neighbor]))

    return [], "N/A", explored

# ---------------- UCS ----------------
def ucs(graph, start, goal):
    pq = [(0, start, [start])]
    visited = set()
    explored = 0

    while pq:
        cost, node, path = heapq.heappop(pq)
        explored += 1

        if node == goal:
            return path, cost, explored

        if node not in visited:
            visited.add(node)

            for neighbor, weight in graph[node].items():
                heapq.heappush(pq,
                               (cost + weight,
                                neighbor,
                                path + [neighbor]))

    return [], float("inf"), explored

# ---------------- A* ----------------
def a_star(graph, start, goal, heuristic):
    pq = [(heuristic[start], 0, start, [start])]
    visited = set()
    explored = 0

    while pq:
        f, g, node, path = heapq.heappop(pq)
        explored += 1

        if node == goal:
            return path, g, explored

        if node not in visited:
            visited.add(node)

            for neighbor, weight in graph[node].items():
                g_new = g + weight
                f_new = g_new + heuristic[neighbor]

                heapq.heappush(
                    pq,
                    (f_new,
                     g_new,
                     neighbor,
                     path + [neighbor])
                )

    return [], float("inf"), explored

# ---------------- MAIN ----------------
start = input("Enter Start Node: ").upper()
goal = input("Enter Goal Node: ").upper()

if start not in graph or goal not in graph:
    print("Invalid Node!")
else:

    results = []

    path, cost, explored = bfs(graph, start, goal)
    results.append(("BFS", path, cost, explored))

    path, cost, explored = ucs(graph, start, goal)
    results.append(("UCS", path, cost, explored))

    path, cost, explored = a_star(graph, start, goal, heuristic)
    results.append(("A*", path, cost, explored))

    print("\n------ Search Algorithm Comparison ------")
    print("{:<10}{:<30}{:<10}{:<15}".format(
        "Algorithm", "Path", "Cost", "Nodes Explored"))

    for algo, path, cost, explored in results:
        print("{:<10}{:<30}{:<10}{:<15}".format(
            algo,
            " -> ".join(path),
            str(cost),
            explored))

    best = min(
        [r for r in results if isinstance(r[2], (int, float))],
        key=lambda x: x[2]
    )

    print("\nBest Algorithm for Shortest Path:", best[0])