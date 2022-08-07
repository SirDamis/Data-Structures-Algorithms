class Solution:
    def countHousePlacements(self, n: int) -> int:
        # memo = {}
        # mod = 10**9 + 7
        # def solve(n, memo):
        #     if n in memo: return memo[n]
        #     if n == 1: return 2
        #     if n == 2: return 3
        #     memo[n] = solve(n-1, memo) + solve(n-2, memo)
        #     return memo[n]
        # return solve(n, memo)**2 % mod

        first, second = 2, 3
        mod = 10 ** 9 + 7
        if n == 1: return first ** 2 % mod
        if n == 2: return second ** 2 % mod

        for idx in range(2, n):
            curr = first + second
            first = second
            second = curr
        return second ** 2 % mod

