class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0])

        def dfs(r, c, row, col):
            # Check out of bound
            if r < 0 or r >= row or c < 0 or c >= col:
                return
            if board[r][c] != '-':
                return

            board[r][c] = 'O'
            dfs(r + 1, c, row, col)
            dfs(r - 1, c, row, col)
            dfs(r, c + 1, row, col)
            dfs(r, c - 1, row, col)

        # Step 1: Replace '0' with '-'
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    board[i][j] = '-'
        # print(board)
        # Step 2: Flood fill the elements on the border which have the value of '-' with '0'
        for m in range(col):
            if board[0][m] == '-':
                dfs(0, m, row, col)
        for m in range(row):
            if board[m][col - 1] == '-':
                dfs(m, col - 1, row, col)

        for m in range(col):
            if board[row - 1][m] == '-':
                dfs(row - 1, m, row, col)

        for m in range(row):
            if board[m][0] == '-':
                dfs(m, 0, row, col)

        # Step 3: Replace all value with '-' with 'X'
        for i in range(row):
            for j in range(col):
                if board[i][j] == '-':
                    board[i][j] = 'X'
