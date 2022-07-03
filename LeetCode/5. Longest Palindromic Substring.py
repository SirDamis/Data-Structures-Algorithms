class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""

        def count(l, r):
            res = ""
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if len(res) < len(s[l:r + 1]):
                    res = s[l:r + 1]
                l -= 1
                r += 1
            return res

        for i in range(len(s)):
            l = r = i
            result = count(l, r) if len(count(l, r)) > len(result) else result

            l, r = i, i + 1
            result = count(l, r) if len(count(l, r)) > len(result) else result

        return result
