class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def solve(n, k, path, res, idx, curr):
            if len(path) == k and curr == n:
                res.append(path)
                return
            if len(path) > k:
                return

            for idx in range(idx, 10):
                solve(n, k, path + [idx], res, idx + 1, curr + idx)

        res = []
        solve(n, k, [], res, idx=1, curr=0)
        return res
