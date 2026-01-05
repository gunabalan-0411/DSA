from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        ROW = len(board)
        COL = len(board[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        def detect_peninsula(r, c):
            # exit condition
            if r < 0 or c < 0 or r >= ROW or c >= COL:
                return
            if board[r][c] != 'O':
                return
            board[r][c] = 'S'
            for dr, dc in directions:
                detect_peninsula(r+dr, c+dc)
        
        for r in range(ROW):
            detect_peninsula(r, 0)
            detect_peninsula(r, COL-1)
        for c in range(COL):
            detect_peninsula(0, c)
            detect_peninsula(ROW-1, c)
        
        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'S':
                    board[r][c] = 'O'

