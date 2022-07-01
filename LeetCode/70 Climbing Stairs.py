class Solution:
    def climbStairs(self, n: int) -> int:
        memo={}
        def solve(n, memo):
            if n in memo:
                return memo[n]
            if n==1: return 1
            if n==2: return 2
            memo[n] = solve(n-1, memo)+solve(n-2, memo)
            return memo[n]
        return solve(n, memo)
