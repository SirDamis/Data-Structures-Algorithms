class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        P   A   H   N
        A P L S I I G
        Y   I   R
        PAHNAPLSIIGYIR
        0: ['', '', ''] id = 0, st= 1
        1: ['P', '', ''] id = 1, st= 1
        2: ['P', 'A', ''] id = 2, st= 1
        3: ['P', 'A', 'Y'] id = 0, st= 0
        4: ['P', 'AP', 'Y'] id = 0, st= 1
        5: ['PA', 'AP', 'Y'] id = 0, st= 1

        """
        if numRows == 1 or numRows >= len(s):
            return s
        res = [''] * numRows
        index, step = 0, 1
        for char in s:
            res[index] += char
            # print(res, index, step)
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step
        return "".join(res)

