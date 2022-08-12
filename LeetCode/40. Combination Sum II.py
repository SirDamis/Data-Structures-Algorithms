class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def solve(candidates, path, res, target):
            if target == 0:
                res.append(path)
                return
            if target < 0: return

            for idx, num in enumerate(candidates):
                if idx > 0 and candidates[idx] == candidates[idx - 1]:
                    continue
                remaining = target - num
                solve(candidates[idx + 1:], path + [candidates[idx]], res, remaining)

        res = []
        solve(sorted(candidates), [], res, target)
        return res
