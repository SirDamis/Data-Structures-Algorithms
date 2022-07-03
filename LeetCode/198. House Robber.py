class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}

        def solve(n, memo):
            if n in memo:
                return memo[n]
            if n < 0:
                return 0
            memo[n] = nums[n] + max(solve(n - 3, memo), solve(n - 2, memo))
            return memo[n]

        return max(solve(n - 1, memo), solve(n - 2, memo))
