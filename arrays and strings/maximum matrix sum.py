class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:

        res = 0
        negative_count = 0

        matrix_minimum = float('inf')

        for row in matrix:
            for n in row:
                res+=abs(n)
            
                matrix_minimum = min(matrix_minimum, abs(n))
                if n<0:
                    negative_count+=1
                
        
        #make the min absolute value positive to maximum sum
        if negative_count%2==1:
            res-=2*matrix_minimum
        
        return res

        
