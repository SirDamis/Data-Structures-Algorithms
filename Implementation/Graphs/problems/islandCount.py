"""
Write a function, islandCount, that takes
in a grid containing Ws and Ls.
W represents water and L represents land.
The function should return the number of
islands on the grid.
An island is vertically or horizontally connected
region of land

r = #row
c = #column
Time Complexity: O(rc)
Space Complexity: O(rc)
"""

def explore(grid, r, c, visited):
    rowInbound = 0 <= r and r < len(grid)
    colInbound = 0 <= c and c < len(grid[0])

    if (not rowInbound) or (not colInbound): return False
    if grid[r][c] == 'W': return False


    pos = (r, c)
    if pos in visited: return False
    visited.add(pos)

    explore(grid, r+1, c, visited)
    explore(grid, r-1, c, visited)
    explore(grid, r, c+1, visited)
    explore(grid, r, c-1, visited)

    return True

def islandCount(grid):
    visited = set()
    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if explore(grid, r, c, visited): count += 1
    return count

grid = [
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'L', 'W'],
    ['W', 'W', 'L', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['L', 'L', 'W', 'W', 'W'],
]
print(islandCount(grid))
