"""
Write a function, largestComponent, that takes in
an adjacency list of an undirected graph.
The function should return the largest connected
components in the graph

n = #nodes
e = #edges
Time Complexity: O(e)
Space Complexity: O(n)

Another ALternative
n = #nodes
n^2 = #edges
Time Complexity: O(n^2)
Space Complexity: O(n)
"""
def explore(graph, current, visited):
    if current in visited: return 0
    visited.add(current)
    count = 1
    for neighbor in graph[current]:
        count += explore(graph, neighbor, visited)
    return count
def largestComponent(graph):
    visited = set()
    largest = 0
    for node in graph:
        current_largest = explore(graph, node, visited)
        largest = max(current_largest, largest)
    return largest


graph = {
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2]
}

print(largestComponent(graph))
