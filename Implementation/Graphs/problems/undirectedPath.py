"""
Write a function, hasPath, that takes in an object
representing the adjacency list of a undirected
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
def buildGraph(edges):
    graph = {}
    for edge in edges:
        a, b = edge
        if a not in graph: graph[a] = []
        if b not in graph: graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph

def hasPathDFT(graph, src, dst, visited):
    if src == dst: return True
    if src in visited: return False
    visited.add(src)
    for neighbor in graph[src]:
        if hasPathDFT(graph, neighbor, dst, visited): return True
    return False

def undirecteed(edges, nodeA, nodeB):
    graph = buildGraph(edges)
    return hasPathDFT(graph, nodeA, nodeB, set())



edges = [
    ['i', 'j'],
    ['k', 'i'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n']
]
print(undirecteed(edges, 'i', 'l'))


