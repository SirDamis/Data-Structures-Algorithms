class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProduct = 1
        minProduct = 1
        result = nums[0]
        for i in range(len(nums)):
            temp = maxProduct * nums[i]
            maxProduct = max(nums[i], minProduct * nums[i], temp)
            minProduct = min(nums[i], minProduct * nums[i], temp)
            result = max(maxProduct, result)
        return result
