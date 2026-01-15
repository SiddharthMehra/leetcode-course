class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n= 9
        rows = [0]*n
        cols = [0]*n
        boxes = [0]*n

        for r in range(n):
            for c in range(n):
                if board[r][c] == ".":
                    continue
                
                pos = int(board[r][c]) -1

                #check row
                if rows[r] & (1<<pos):
                    return False
                
                rows[r] |= 1<<pos

                #check column
                if cols[c] & (1<<pos):
                    return False
                cols[c] |= 1<<pos

                idx = (r//3) * 3 + c//3
                if boxes[idx] & (1<<pos):
                    return False
                
                #check box
                boxes[idx] |= 1<<pos
        
        return True
