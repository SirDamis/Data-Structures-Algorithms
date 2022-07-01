"""
    a -> c
    |    |
    *    *
    b    e
    |
    *
    d -> f

    Breadth First Traversal: a -> b -> c -> d -> e -> f
    Uses a Queue
"""
from collections import deque

def breadthFirstPrint(graph, source):
    queue = deque()
    queue.append(source)

    while queue:
        curr = queue.popleft()
        print(curr)
        for neighbor in graph[curr]:
            queue.append(neighbor)


graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
    }
breadthFirstPrint(graph, 'a')
