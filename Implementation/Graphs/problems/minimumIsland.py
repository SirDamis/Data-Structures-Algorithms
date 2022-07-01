"""
Write a function, minimumIsland, that takes
in a grid containing Ws and Ls.
W represents water and L represents land.
The function should return the size of
smallest island
An island is vertically or horizontally connected
region of land
Assume that grid contains at least an island


r = #row
c = #column
Time Complexity: O(rc)
Space Complexity: O(rc)
"""
def exploreSize(grid, r, c, visited):
    rowInbound = 0 <= r and r < len(grid)
    colInbound = 0 <= c and c < len(grid[0])

    if (not rowInbound) or (not colInbound): return 0
    if grid[r][c] == 'W': return 0

    pos = (r, c)
    if pos in visited: return 0

    visited.add(pos)
    size = 1
    size += exploreSize(grid, r + 1, c, visited)
    size += exploreSize(grid, r - 1, c, visited)
    size += exploreSize(grid, r, c + 1, visited)
    size += exploreSize(grid, r, c - 1, visited)
    return  size

def minimumIsland(grid):
    visited = set()
    min_size = float('inf')

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            size =  exploreSize(grid, r, c, visited)
            if size > 0:
                min_size = min(min_size, size)
    return min_size

grid = [
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'L', 'W'],
    ['W', 'W', 'L', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['L', 'L', 'W', 'W', 'W'],
]
print(minimumIsland(grid))
