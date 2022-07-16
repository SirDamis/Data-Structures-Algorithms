class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if len(digits) == 0:
            return res

        hashmap = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def solve(digits, index, path, res, hashmap):
            if index == len(digits):
                res.append(path)
                return

            strings = hashmap[digits[index]]
            for string in strings:
                solve(digits, index + 1, path + string, res, hashmap)

        solve(digits, 0, '', res, hashmap)
        return res



