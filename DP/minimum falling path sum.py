class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        for r in range(1, len(matrix)):
            for c in range(len(matrix[0])):
                #first column, above or right across, left across is not possible
                if c == 0:
                    matrix[r][c]+=min(matrix[r-1][c], matrix[r-1][c+1])
                
                #last column, above or left across, right across is not possible
                elif c == len(matrix[0]) - 1:
                    matrix[r][c]+=min(matrix[r-1][c], matrix[r-1][c-1])
                
                #otherwise try all 3 combinations
                else:
                    matrix[r][c] +=min(matrix[r-1][c], matrix[r-1][c+1], matrix[r-1][c-1])
        
        return min(matrix[-1])
                

        
