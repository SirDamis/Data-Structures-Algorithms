class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def solve(s, op, close, n):
            if len(s) == n * 2:
                res.append(s)
                return
            if op < n:
                solve(s + '(', op + 1, close, n)
            if close < op:
                solve(s + ')', op, close + 1, n)

        solve('', 0, 0, n)
        return res
