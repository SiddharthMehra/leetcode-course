class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        posDiag = set()
        antiDiag = set()

        res = []
        board = [["."] * n for i in range(n)]

        #place only 1 queen per row
        def backtrack(r):
            if r==n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in cols or (r+c) in posDiag or (r-c) in antiDiag:
                    continue
                
                cols.add(c)
                posDiag.add(r+c)
                antiDiag.add(r-c)
                board[r][c] = 'Q'

                backtrack(r+1)

                cols.remove(c)
                posDiag.remove(r+c)
                antiDiag.remove(r-c)
                #restore state
                board[r][c] = "."

        backtrack(0)
        return res



