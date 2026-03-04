from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW = len(board)
        COL = len(board[0])
        # to avoid repeated paths from same origin
        visited = set()
        # to search in all four directions
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        word_len = len(word)

        # Depth First search based recurssion
        def dfs(i, r, c):
            # -- Base condition to exist
            # Search success exist condition
            if i == word_len:
                return True
            # Search fail exist condition
            if (
                r < 0
                or c < 0
                or r >= ROW
                or c >= COL
                or word[i] != board[r][c]
                or (r, c) in visited
            ):
                return False

            visited.add((r, c))
            # recursive iterate in all directions
            result = False
            for dr, dc in directions:
                result |= dfs(i + 1, r + dr, c + dc)
            visited.remove((r, c))

            return result

        # Brute force to start from every point as origin point
        for r in range(ROW):
            for c in range(COL):
                if dfs(0, r, c):
                    return True
        return False
