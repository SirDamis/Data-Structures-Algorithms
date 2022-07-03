class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        i = len(obstacleGrid) - 1
        j = len(obstacleGrid[0]) - 1
        memo = {}

        def solve(m, n, memo):
            pos = m, n
            if pos in memo:
                return memo[pos]
            if m > i or n > j: return 0
            if obstacleGrid[m][n] == 1: return 0
            if m == i and n == j:
                return 1

            memo[pos] = solve(m + 1, n, memo) + solve(m, n + 1, memo)
            return memo[pos]

        return solve(0, 0, memo)
