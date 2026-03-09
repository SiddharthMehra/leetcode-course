class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])

        pre = [[0] * (n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                pre[i][j] = (mat[i-1][j-1] + pre[i-1][j] + pre[i][j-1] - pre[i-1][j-1])
        
        def squaresum(r, c, k):
            return (pre[r+k][c+k] - pre[r+k][c] - pre[r][c+k] + pre[r][c])
        
        max_side = 0

        for k in range(1, min(m,n) + 1):
            found = False
            for i in range(m-k+1):
                for j in range(n-k+1):
                    if squaresum(i, j, k)<=threshold:
                        max_side = k
                        found = True
                        break
                    
                if found:
                    break
            
        return max_side
