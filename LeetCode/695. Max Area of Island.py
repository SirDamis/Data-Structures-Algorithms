class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def checkGrid(row, col, visited):
            pos = (row, col)
            # Out of bound
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                return 0
            # Avoid endless loop
            if pos in visited:
                return 0

            if grid[row][col] == 0:
                return 0
            visited.add(pos)
            current = 1
            current += checkGrid(row + 1, col, visited)
            current += checkGrid(row - 1, col, visited)
            current += checkGrid(row, col + 1, visited)
            current += checkGrid(row, col - 1, visited)
            return current

        def solve(grid):
            visited = set()
            result = 0
            for row in range(len(grid)):
                for col in range(len(grid[0])):
                    result = max(result, checkGrid(row, col, visited))
            return result

        return solve(grid)
