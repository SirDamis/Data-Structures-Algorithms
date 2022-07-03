class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def solve(s):
            if s in memo: return memo[s]
            if len(s) > 0 and s[0] == '0': return 0
            if len(s) == 1 or s == '': return 1
            if int(s[:2]) <= 26:
                memo[s] = solve(s[1:]) + solve(s[2:])
                return memo[s]
            else:
                memo[s] = solve(s[1:])
                return memo[s]

        return solve(s)
