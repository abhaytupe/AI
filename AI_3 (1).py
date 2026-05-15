# Greedy Algorithms
## Artificial Intelligence Practical
## Aim

# Implement Greedy Algorithms:
# 1. Selection Sort
# 2. Prim's Minimum Spanning Tree
# 3. Dijkstra's Shortest Path Algorithm

## Aim

# Implement Greedy Algorithms:
# 1. Selection Sort
# 2. Prim's Minimum Spanning Tree
# 3. Dijkstra's Shortest Path Algorithm
## 1. Selection Sort

# Selection Sort repeatedly selects the minimum element and places it at the correct position.
# Selection Sort

# Step_1

arr = [64, 25, 12, 22, 11]

n = len(arr)

for i in range(n):

    min_index = i

    for j in range(i + 1, n):

        if arr[j] < arr[min_index]:
            min_index = j

    arr[i], arr[min_index] = arr[min_index], arr[i]

print("Sorted Array:")
print(arr)
## 2. Prim's Minimum Spanning Tree Algorithm

# Prim's algorithm finds the minimum spanning tree of a weighted graph.
# Prim's Algorithm

# Step_2

INF = 9999999

N = 5

graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

selected = [0, 0, 0, 0, 0]

selected[0] = True

print("Edge : Weight")

for i in range(N - 1):

    minimum = INF
    x = 0
    y = 0

    for i in range(N):

        if selected[i]:

            for j in range(N):

                if (not selected[j]) and graph[i][j]:

                    if minimum > graph[i][j]:
                        minimum = graph[i][j]
                        x = i
                        y = j

    print(x, "-", y, ":", graph[x][y])

    selected[y] = True
## 3. Dijkstra's Shortest Path Algorithm

# Dijkstra's algorithm finds the shortest distance from a source node to all other nodes.
# Dijkstra Algorithm

# Step_3

import heapq

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

def dijkstra(graph, start):

    priority_queue = [(0, start)]

    distances = {node: float('inf') for node in graph}

    distances[start] = 0

    while priority_queue:

        current_distance, current_node = heapq.heappop(priority_queue)

        for neighbor, weight in graph[current_node].items():

            distance = current_distance + weight

            if distance < distances[neighbor]:

                distances[neighbor] = distance

                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

result = dijkstra(graph, 'A')

print("Shortest Distances:")
print(result)
## Conclusion

# Greedy algorithms make the best possible choice at each step.
# Selection Sort, Prim's Algorithm, and Dijkstra's Algorithm were implemented successfully.
# ## Conclusion

# Greedy algorithms make the best possible choice at each step.
# Selection Sort, Prim's Algorithm, and Dijkstra's Algorithm were implemented successfully.
