"""
Write a function, hasPath, that takes in an object
representing the adjacency list of a directed acyclic
graph and two nodes (src, dist).
The function should return a boolean indicating whether
or not there exists a directed path between the source
and destination nodes.

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

def hasPathDFT(graph, src, dst):
    if src == dst:
        return True
    for neighbor in graph[src]:
        if hasPathDFT(graph, neighbor, dst):
            return True
    return False

from collections import  deque
def hasPathBFT(graph, src, dst):
    queue = deque()
    queue.append(src)

    while queue:
        curr = queue.popleft()
        if curr == dst:
            return True
        for neighbor in graph[curr]:
            queue.append(neighbor)
    return False
graph = {
    'f': ['g', 'i'],
    'g': ['h'],
    'h': [],
    'i': ['g', 'k'],
    'j': ['i'],
    'k': []
}
# print(hasPathDFT(graph, 'h', 'k'))
print(hasPathBFT(graph, 'f', 'k'))
