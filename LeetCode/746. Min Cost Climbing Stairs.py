class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {}

        def solve(cost, n, memo):
            if n in memo:
                return memo[n]
            if n == 0:
                return cost[0]
            if n == 1:
                return cost[1]
            memo[n] = cost[n] + min(solve(cost, n - 1, memo), solve(cost, n - 2, memo))
            return memo[n]

        return min(solve(cost, n - 1, memo), solve(cost, n - 2, memo))
