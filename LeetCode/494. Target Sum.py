class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # def solve(nums, lastSum):
        #     if len(nums) == 0:
        #         if lastSum == target:
        #             return 1
        #         return 0
        #     res = 0
        #     res += solve(nums[1:], lastSum+nums[0])
        #     res += solve(nums[1:], lastSum-nums[0])
        #     return res
        # return solve(nums, 0)

        #         def solve(nums, index, currSum, memo):
        #             string = (index, currSum)
        #             if string in memo:
        #                 return memo[string]
        #             if len(nums) == index:
        #                 if currSum == target:
        #                     return 1
        #                 return 0
        #             res = 0
        #             res += solve(nums, index+1, currSum+nums[index], memo)
        #             res += solve(nums, index+1, currSum-nums[index], memo)
        #             memo[string] =  res
        #             return memo[string]
        #         memo = {}
        #         return solve(nums, 0, 0, memo)

        def solve(nums, lastSum, memo, index):
            string = (index, lastSum)
            if string in memo:
                return memo[string]

            if len(nums) == 0:
                if lastSum == target:
                    return 1
                return 0
            res = 0
            res += solve(nums[1:], lastSum + nums[0], memo, index + 1)
            res += solve(nums[1:], lastSum - nums[0], memo, index + 1)
            memo[string] = res
            return memo[string]

        memo = {}
        return solve(nums, 0, memo, 0)
