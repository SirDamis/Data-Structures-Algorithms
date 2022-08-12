class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # def solve(curr, res, left, right):
        #     print(left, right, curr)
        #     if not right:
        #         res.append(curr)
        #         return
        #     if left:
        #         solve(curr+"(", res, left-1, right)
        #     if right>left:
        #         solve(curr+")", res, left, right-1)
        # res = []
        # solve("", res, n, n)
        def solve(curr, res, left, right, n):
            print(left, right, curr)
            if len(curr) == n*2:
                res.append(curr)
                return
            if left<n:
                solve(curr+"(", res, left+1, right, n)
            if left>right:
                solve(curr+")", res, left, right+1, n)
        res = []
        solve("", res, 0, 0, n)
        return res
