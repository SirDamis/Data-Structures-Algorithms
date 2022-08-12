class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def solve(nums, path, res):
            if not nums:
                res.append(path)
                return
            for idx in range(len(nums)):
                if idx > 0 and nums[idx] == nums[idx - 1]:
                    continue
                solve(nums[:idx] + nums[idx + 1:], path + [nums[idx]], res)

        res = []
        solve(sorted(nums), [], res)
        return res
