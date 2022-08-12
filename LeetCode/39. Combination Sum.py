class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def solve(candidates, path, res, target):
            if target == 0:
                res.append(path)
                return
            if target < 0: return

            for idx, num in enumerate(candidates):
                remaining = target - num
                solve(candidates[idx:], path + [candidates[idx]], res, remaining)

        res = []
        solve(candidates, [], res, target)
        return res
