# A* Search Algorithm
## Artificial Intelligence Practical

## Aim

# Implement A* Search Algorithm for path finding problem.
# from queue import PriorityQueue

# Graph with heuristic values
graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 3, 'E': 1},
    'C': {'F': 5},
    'D': {},
    'E': {'F': 1},
    'F': {}
}

# Heuristic values
heuristic = {
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 3,
    'E': 1,
    'F': 0
}

def a_star(start, goal):

    pq = PriorityQueue()
    pq.put((0, start))

    cost = {start: 0}
    parent = {start: None}

    while not pq.empty():

        current = pq.get()[1]

        if current == goal:
            break

        for neighbor in graph[current]:

            new_cost = cost[current] + graph[current][neighbor]

            if neighbor not in cost or new_cost < cost[neighbor]:

                cost[neighbor] = new_cost

                priority = new_cost + heuristic[neighbor]

                pq.put((priority, neighbor))

                parent[neighbor] = current

    # Reconstruct path
    path = []
    node = goal

    while node is not None:
        path.append(node)
        node = parent[node]

    path.reverse()

    print("Shortest Path:", path)
    print("Total Cost:", cost[goal])

# Function call
a_star('A', 'F')
## Theory

# A* algorithm is an informed search algorithm used to find the shortest path.
# It combines:
# - Actual cost from start node
# - Heuristic estimated cost to goal node

# Formula:
# f(n) = g(n) + h(n)

# Where:
# g(n) = actual path cost
# h(n) = heuristic value
## Conclusion

# The A* Search Algorithm successfully found the shortest path between the start and goal node.
