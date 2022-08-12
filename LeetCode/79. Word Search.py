class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False

        def dfs(board, i, j, word):
            if not word:
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
                return False
            # if (i, j) in visited:
            #     return False

            # Track visited path
            tmp = board[i][j]
            board[i][j] = "#"
            # visited.add((i,j))
            result = dfs(board, i - 1, j, word[1:]) + dfs(board, i + 1, j, word[1:]) + dfs(board, i, j - 1,
                                                                                           word[1:]) + dfs(board, i,
                                                                                                           j + 1,
                                                                                                           word[1:])
            # remove visited path
            board[i][j] = tmp
            # visited.remove((i,j))
            return result

        # visited = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(board, i, j, word):
                    return True
        return False
