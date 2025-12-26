class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def valid(x, y):
            return 0<=x<rows and 0<=y<cols

        def backtrack(row, col, i, seen):
            if i == len(word):
                return True
            
            for dx, dy in directions:
                next_row, next_col = row+dx, col+dy
                if valid(next_row, next_col) and (next_row, next_col) not in seen:
                    if board[next_row][next_col] == word[i]:
                        seen.add((next_row, next_col))
                        if backtrack(next_row, next_col, i+1, seen):
                            return True
                        seen.remove((next_row, next_col))
            
            return False
        
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0] and backtrack(row, col, 1, {(row, col)}):
                    return True
        
        return False



