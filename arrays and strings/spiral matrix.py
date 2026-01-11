class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        row, col = 0, 0
        #default position, move right
        drow, dcol = 0, 1
        res = []

        for _ in range(rows*cols):
            res.append(matrix[row][col])
            #mark cell as visited
            matrix[row][col] = "."

            #turn right clockwise if you are at last row or col
            if not (0 <= row + drow < rows and 0 <= col + dcol < cols) \
               or matrix[row + drow][col + dcol] == ".":
                drow, dcol = dcol, -drow  # turn clockwise
            
            row+=drow
            col+=dcol
        
        return res





