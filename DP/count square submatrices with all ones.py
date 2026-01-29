class Solution:
    def countSquares(self, A):
        if not A:
            return 0
        
        rows, cols = len(A), len(A[0])
        dp = [[0] * cols for _ in range(rows)]

        res = 0

        for r in range(rows):
            for c in range(cols):
                if A[r][c]:
                    if r==0 or c==0:
                        dp[r][c] = 1
                    else:
                        #check all neighbors
                        dp[r][c] = 1 + min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1])  

                    res+=dp[r][c]

        return res      
        
