class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        size = len(nums)
        if nums[0] != 0:
            return 0
        for i in range(0, size - 1):
            if nums[i + 1] - nums[i] != 1:
                return nums[i] + 1
        return nums[size - 1] + 1

        # size = arr_len= len(nums)
        # i = 0
        # while i < arr_len:
        #     size += (i - nums[i])
        #     i += 1
        # return size



