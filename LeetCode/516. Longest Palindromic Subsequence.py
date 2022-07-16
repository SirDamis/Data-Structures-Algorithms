class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        #         def solve(s):
        #             text1 = s
        #             text2 = s[::-1]
        #             dp  = [[0 for j in range(len(text1)+1)] for i in range(len(text2)+1)]
        #             for i in range(len(text2)-1, -1, -1):
        #                 for j in range(len(text1)-1, -1, -1):
        #                     if text2[i] == text1[j]:
        #                         dp[i][j] = 1 + dp[i+1][j+1]
        #                     else:
        #                         dp[i][j] = max(dp[i][j+1], dp[i+1][j])

        #             return dp[0][0]

        def solve(s):
            dp = [[0 for j in range(len(s))] for i in range(len(s))]

            for i in range(len(s) - 1, -1, -1):
                dp[i][i] = 1
                for j in range(i + 1, len(s)):
                    if s[i] == s[j]:
                        dp[i][j] = dp[i + 1][j - 1] + 2
                    else:
                        dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
                    print(i, j)
            return dp[0][len(s) - 1]

        return solve(s)
