class Solution:
    def solve(self, board):
        rows = len(board)
        cols = len(board[0])

        def dfs(r, c):
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                board[r][c] != "O"
            ):
                return

            # Mark edge-connected O as safe
            board[r][c] = "S"

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Check the first and last columns
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)

        # Check the first and last rows
        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)

        # Capture surrounded regions
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "S":
                    board[r][c] = "O"