class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Time Complexity: O(nlogn), Space Complexity: O(1)
        nums.sort()
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        initial = 0
        for i in range(0, len(nums)):
            if nums[i] == 0 :
                continue
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i]-initial != 1:
                return initial + 1
            else:
                initial =  nums[i]
        return nums[i]+1
