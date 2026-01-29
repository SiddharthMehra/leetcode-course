class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:

        ans = 0
        squareOfDiag= 0
        max_diag= 0

        for l, w in dimensions:
            squareOfDiag = l*l + w*w
            area = l*w
            if squareOfDiag> max_diag:
                max_diag = squareOfDiag
                max_area = area
            
            elif squareOfDiag == max_diag:
                max_area = max(max_area, area)
        
        return max_area

        
