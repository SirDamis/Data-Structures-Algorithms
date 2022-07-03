class Solution:
    def explore(self, grid, r, c, visited):
        pos = (r, c)

        # Out of bound
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
            return False
        if grid[r][c] == '0':
            return False
        if pos in visited:
            return False
        visited.add(pos)

        self.explore(grid, r + 1, c, visited)
        self.explore(grid, r - 1, c, visited)
        self.explore(grid, r, c + 1, visited)
        self.explore(grid, r, c - 1, visited)
        return True

    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if self.explore(grid, r, c, visited):
                    count += 1
        return count
