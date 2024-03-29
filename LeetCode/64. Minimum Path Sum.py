class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        def solve(grid):
            row = len(grid)
            col = len(grid[0])

            for i in range(row):
                for j in range(col):
                    if i == 0 and j == 0:
                        continue
                    elif i == 0:
                        grid[i][j] += grid[i][j - 1]
                    elif j == 0:
                        grid[i][j] += grid[i - 1][j]
                    else:
                        grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
            return grid[row - 1][col - 1]

        return solve(grid)
