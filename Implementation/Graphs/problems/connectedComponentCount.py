"""
Write a function, connectedComponetCount, that takes in
an adjacency list of an undirected graph.
The function should return the number of connected
components within the graph

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
    if current in visited: return False
    visited.add(current)
    for neighbor in graph[current]:
        explore(graph, neighbor, visited)
    return True

def connectedComponetCount(graph):
    visited = set()
    count = 0
    for node in graph:
        if explore(graph, node, visited): count += 1
    return count

graph = {
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2]
}
print(connectedComponetCount(graph))
