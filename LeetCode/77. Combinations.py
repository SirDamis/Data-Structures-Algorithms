class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def solve(n, k, path, res, idx):
            if not k:
                res.append(path)
                return

            for idx in range(idx, n + 1):
                solve(n, k - 1, path + [idx], res, idx + 1)

        res = []
        solve(n, k, [], res, 1)
        return res


