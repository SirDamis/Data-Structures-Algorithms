"""
    Depth First Traversal
    a -> c
    |    |
    *    *
    b    e
    |
    *
    d -> f

    Depth First Traversal:
     a -> b -> d -> f -> c -> e
     OR
     a -> c -> e ->b -> d -> f
    Uses a Stack
"""
def depthFirstPrint(graph, source):
    stack = [source]

    while stack:
        curr = stack.pop()
        print(curr)
        for neighbor in graph[curr]:
            stack.append(neighbor)

def depthFirstRecursion(graph, source):
    """
    Using recursion.
    It utilizes a stack as well
    :param graph:
    :param source:
    :return:
    """
    print(source)
    for neighbor in graph[source]:
        depthFirstRecursion(graph, neighbor)

graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
    }

# depthFirstPrint(graph, 'a')
depthFirstRecursion(graph, 'a')
