class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        currSum = 0
        maxPrefix = 0
        minPrefix = 0

        for num in nums:
            currSum += num
            maxPrefix = max(maxPrefix, currSum)
            minPrefix = min(minPrefix, currSum)
        return maxPrefix - minPrefix
