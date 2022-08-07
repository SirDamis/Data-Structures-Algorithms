class Solution:
    def tribonacci(self, n: int) -> int:
        # memo = {
        #     0:0,
        #     1:1,
        #     2:1
        # }
        # def solve(n, memo):
        #     if n in memo: return memo[n]
        #     memo[n] = solve(n-1, memo) + solve(n-2, memo) + solve(n-3, memo)
        #     return memo[n]
        # return solve(n, memo)
        if n == 0 or n == 1: return n
        if n == 2: return 1

        first, second, third = 0, 1, 1
        for _ in range(3, n + 1):
            total = first + second + third
            first = second
            second = third
            third = total
        return total
