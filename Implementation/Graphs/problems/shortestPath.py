"""
Write a function, shortestPath, that takes
in an array of edges for an undirected graph
and two nodes (nodeA, nodeB).
The function should return the length of
the shortest path between A and B.
Consider the length as the number of edges
is the path and not the number of nodes.
If there is no path between A and B, return
-1

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
from collections import deque

def buildGraph(edges):
    graph = {}
    for edge in edges:
        a, b = edge
        if a not in graph: graph[a] = []
        if b not in graph: graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph


def shortestPath(edges, nodeA, nodeB):
    graph = buildGraph(edges)
    visited = set()

    queue = deque()
    queue.append([nodeA, 0])
    visited.add(nodeA)

    while queue:
        node, distance = queue.popleft()
        if node == nodeB: return distance

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append([neighbor, distance+1])
    return -1


edges = [
    ['a', 'c'],
    ['a', 'b'],
    ['c', 'b'],
    ['c', 'd'],
    ['b', 'd'],
    ['e', 'd'],
    ['g', 'f']
]
print(shortestPath(edges, 'a', 'y'))
