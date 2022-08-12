class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def solve(nums, path, res):
            if not nums:
                res.append(path)
                return

            for idx, num in enumerate(nums):
                solve(nums[:idx] + nums[idx + 1:], path + [nums[idx]], res)

        res = []
        solve(nums, [], res)
        return res
