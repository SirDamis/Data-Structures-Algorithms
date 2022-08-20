"""
Given a string, find the longest palindromic substring. If there are more than one with the maximum length
return any one.

Example: Input: aabcdcb, Output: bcdcb
         Input: banana, Output: anana
"""
import unittest


def longestPalindromicSubstring(s):
    n = len(s)
    longest = ""
    for i in range(n):
        l, r = i, i
        while l >= 0 and r < n and s[l] == s[r]:
            if len(s[l:r+1]) > len(longest):
                longest = s[l:r+1]
            l -= 1
            r += 1

        l, r = i, i+1
        while l >= 0 and r < n and s[l] == s[r]:
            if len(s[l:r+1]) > len(longest):
                longest = s[l:r+1]
            l -= 1
            r += 1
    return longest

class CodeTest(unittest.TestCase):
    def testEvenLength(self):
        longest = longestPalindromicSubstring("aaabac")
        self.assertEqual(longest, 'aaa')
    def testOddLength(self):
        longest = longestPalindromicSubstring("aaabacaba")
        self.assertEqual(longest, 'abacaba')
if __name__ == '__main__':
    unittest.main()


