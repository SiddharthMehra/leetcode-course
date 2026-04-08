class Solution:
    def tourOfKnight(self, m: int, n: int, r: int, c: int) -> List[List[int]]:

        board = [[-1 for _ in range(n)] for _ in range(m)]

        #possible knight moves
        moves = [(2,1), (1,2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1,-2), (2,-1)]

        def is_valid(x, y):
            return 0<=x<m and 0<=y<n and board[x][y] == -1
        
        def backtrack(x, y, step):

            if step == m*n:
                return True
            
            for dx, dy in moves:
                nx, ny = x+dx, y+dy

                if is_valid(nx, ny):
                    board[nx][ny] = step

                    if backtrack(nx, ny, step+1):
                        return True
                    
                    board[nx][ny] = -1
            
            return False
        
        board[r][c] = 0
        if backtrack(r, c, 1):
            return board
        else:
            return []
        
