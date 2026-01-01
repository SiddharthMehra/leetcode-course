class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row, diagonals, anti_diagonals, cols):
            if row == n:
                return 1
        
            solutions = 0
            for col in range(n):
                curr_diagonal = 1<<(row-col+n) #added n to prevent it being negative
                curr_anti_diagonal = 1<<(row+col)
                curr_col = 1<<col

                #check if bits are set
                if (cols & curr_col ) or \
                (diagonals & curr_diagonal) or \
                (anti_diagonals  & curr_anti_diagonal):
                    continue

                #add the queen to the board(XOR sets the bit on)
                cols^=curr_col
                diagonals^=curr_diagonal
                anti_diagonals^=curr_anti_diagonal

                solutions+=backtrack(row+1, diagonals, anti_diagonals, cols)

                #remove the queen from the board(XOR sets the bit off)
                cols^=curr_col
                diagonals^=curr_diagonal
                anti_diagonals^=curr_anti_diagonal

            return solutions
        
        return backtrack(0,0,0,0)

