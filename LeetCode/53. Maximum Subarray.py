class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # # Using Brute Approach: Time Limit Exceeded
        # maxSum = float('-inf')
        # for i in range(len(nums)):
        #     currentSum = 0
        #     for j in range(i, len(nums)):
        #         currentSum +=nums[j]
        #         maxSum = max(currentSum, maxSum)
        # return maxSum

        # Using sliding window
        maxSum = nums[0]
        currSum = 0

        for num in nums:
            if currSum < 0:
                currSum = 0
            currSum += num
            maxSum = max(currSum, maxSum)
        return maxSum
