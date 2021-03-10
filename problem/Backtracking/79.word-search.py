#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:
    row, col = 0, 0
    board = None

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.row, self.col = len(board), len(board[0])
        self.board = board
        self.word = word

        for r in range(self.row):
            for c in range(self.col):
                if self.dfs(r, c, 0):
                    return True
        return False

    # DFS
    def dfs(self, r, c, i):
        if not self.boundary_valid(r, c):
            return False
        if self.word[i] != self.board[r][c]:
            return False
        if i == len(self.word)-1:
            return True
        char = self.board[r][c]
        self.board[r][c] = 0
        found = self.dfs(r-1, c, i+1) or self.dfs(r+1, c, i+1) \
            or self.dfs(r, c-1, i+1) or self.dfs(r, c+1, i+1)
        self.board[r][c] = char
        return found

    def boundary_valid(self, r, c):
        if r < 0 or r >= self.row or \
                c < 0 or c >= self.col:
            return False
        return True
        # @lc code=end
