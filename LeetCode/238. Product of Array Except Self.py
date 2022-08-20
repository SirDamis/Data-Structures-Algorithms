class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #         #Approach 2: Use Prefix and Postfix Product
        #         n = len(nums)
        #         prefix, postfix = [1]*n, [1]*n

        #         initial = 1
        #         for idx in range(len(nums)):
        #             temp = nums[idx]
        #             prefix[idx] = initial
        #             initial = temp*initial

        #         initial = 1
        #         for idx in range(len(nums)-1, -1, -1):
        #             postfix[idx] = initial
        #             initial = nums[idx]*postfix[idx]
        #         for idx in range(len(nums)):
        #             nums[idx] = postfix[idx]*prefix[idx]
        #         return nums
        # Approach 2 Space Optimized: Use Prefix and Postfix Product
        n = len(nums)
        prefix = [1] * n

        initial = 1
        for idx in range(len(nums)):
            temp = nums[idx]
            prefix[idx] = initial
            initial = temp * initial

        postfix = 1
        print(prefix)
        for idx in range(len(nums) - 1, -1, -1):
            prefix[idx] *= postfix
            postfix *= nums[idx]
        return prefix
