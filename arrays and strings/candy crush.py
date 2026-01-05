#simulation
class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        rows, cols = len(board), len(board[0])

        while True:
            crushed = False

            #horizontal crush
            for r in range(rows):
                for c in range(cols-2):
                    val = abs(board[r][c])
                    if val!=0 and abs(board[r][c+1]) == val and abs(board[r][c+2]) == val:
                        board[r][c] = board[r][c+1] = board[r][c+2] = -val
                        crushed = True
            
            #vertical crush
            for r in range(rows-2):
                for c in range(cols):
                    val = abs(board[r][c])
                    if val!=0 and abs(board[r+1][c]) == val and abs(board[r+2][c]) == val:
                        board[r][c] = board[r+1][c] = board[r+2][c] = -val
                        crushed = True
            
            if not crushed:
                break
            
            #set crushed candies to 0 which means they are crushed, not to be considered in future
            for r in range(rows):
                for c in range(cols):
                    if board[r][c]<0:
                        board[r][c] = 0
            
            #write all non zero(non crushed candies to the bottom)
            for c in range(cols):
                write_row = rows -1
                for r in range(rows-1, -1, -1):
                    if board[r][c]!=0:
                        board[write_row][c] = board[r][c]
                        write_row-=1
                
                #fill all remaining elements with 0(empty space)
                for r in range(write_row, -1, -1):
                    board[r][c] = 0
            
        return board

            


        
