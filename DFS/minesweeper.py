class Solution(object):
    def updateBoard(self, board, click):

        rows, cols = len(board), len(board[0])
        r, c = click

        if board[r][c] == 'M':
            board[r][c] = 'X'
            return board
        
        directions = [(-1, -1),(-1, 0),(-1, 1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

        def dfs(r, c):
            #count adjacent mines
            mines = 0
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if 0<=nr<rows and 0<=nc<cols:
                    if board[nr][nc] == 'M':
                        mines+=1
            
            if mines>0:
                board[r][c] = str(mines)
                return
            
            #otherwise mark as blank and expand
            board[r][c] = 'B'

            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if 0<=nr<rows and 0<=nc<cols:
                    if board[nr][nc] == 'E':
                        dfs(nr, nc)
        
        dfs(r, c)
        return board
                
