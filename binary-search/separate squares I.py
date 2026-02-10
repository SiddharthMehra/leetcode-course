class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:

        low = min(y for _, y, _ in squares)
        high = max(y+l for _, y, l in squares)

        def diff(Y):
            below = above = 0.0
            for _, y, l in squares:
                #entire square below the line
                if y+l<=Y:
                    below+=l*l
                elif y>=Y:
                    above+=l*l
                else:
                    below+=l * (Y - y)
                    above+=l * (y+l - Y)
            
            return below - above
        
        for _ in range(60):
            mid = (low+high)/2
            if diff(mid)<0:
                low = mid
            else:
                high = mid
        
        return (low+high)/2
        
