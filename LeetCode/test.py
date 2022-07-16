class Solution:
    def reverseVowels(self, s: str) -> str:
        l, r = 0, len(s) - 1

        print(l)
        if s[l]  not in 'aeiou':
            print('Yes')
            l += 1
            print(l)

        while l < r:
            print(l, r)
            if s[l] not in 'aeiou':
                l += 1
            elif s[r] not in 'aeiou':
                r -= 1
            if s[r] in 'aeiou' and s[l] in 'aeiou' and s[l] == s[r]:
                l += 1
                r -= 1

        return s

s = Solution()
res = s.reverseVowels('leo')
print(res)
