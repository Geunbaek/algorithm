from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(a, b, depth):
            if depth >= len(word):
                return True

            if a < 0 or a >= len(board[0]) or b < 0 or b >= len(board):
                return False

            if word[depth] != board[b][a]:
                return False

            temp = board[b][a]
            board[b][a] = '0'
            ret = dfs(a + 1, b, depth + 1) or dfs(a - 1, b, depth + 1) or dfs(a, b + 1, depth + 1) or dfs(a, b - 1,
                                                                                                          depth + 1)
            board[b][a] = temp

            return ret

        for y in range(len(board)):
            for x in range(len(board[y])):
                if dfs(x, y, 0):
                    return True
        return False
