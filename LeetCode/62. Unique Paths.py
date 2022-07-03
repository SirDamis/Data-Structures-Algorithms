class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def solve(row, col,memo):
            n = row,col
            if n in memo:
                return memo[n]
            if row == 0 or col == 0: return 1
            if row <0 or col<0: return 0
            memo[n] = solve(row-1, col, memo) + solve(row, col-1, memo)
            return memo[n]
        return solve(m-1, n-1, {})
