class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def solve(s, path, res):
            def isPalindrome(s):
                return s == s[::-1]

            if not s:
                res.append(path)
                return

            for i in range(1, len(s) + 1):
                if isPalindrome(s[:i]):
                    solve(s[i:], path + [s[:i]], res)

        res = []
        solve(s, [], res)
        return res

