class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0

        def count(l, r):
            res = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            return res

        for i in range(len(s)):
            l = r = i
            result += count(l, r)

            l, r = i, i + 1
            result += count(l, r)

        return result

