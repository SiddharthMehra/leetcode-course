class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])

        row_prefix = [[0] * (n+1) for _ in range(m)]
        col_prefix = [[0] * n for _ in range(m+1)]

        for r in range(m):
            for c in range(n):
                row_prefix[r][c+1] = row_prefix[r][c]+ grid[r][c]
                col_prefix[r+1][c] = col_prefix[r][c] + grid[r][c]
        
        max_k = min(m, n)

        for k in range(max_k, 0, -1):
            for r in range(m-k+1):
                for c in range(n-k+1):

                    target = row_prefix[r][c+k] - row_prefix[r][c]

                    #check rows
                    ok = True
                    for i in range(k):
                        if row_prefix[r+i][c+k] - row_prefix[r+i][c]!=target:
                            ok = False
                            break
                    if not ok:
                        continue
                    #check columns
                    ok = True
                    for j in range(k):
                        if col_prefix[r+k][c+j] - col_prefix[r][c+j]!=target:
                            ok = False
                            break
                    
                    if not ok:
                        continue
                    
                    #main diagonal
                    diag1 = sum(grid[r+i][c+i] for i in range(k))
                    if diag1!=target:
                        continue
                    
                    #anti diagonal
                    diag2 = sum(grid[r+i][c+k-1-i] for i in range(k))
                    if diag2!=target:
                        continue
                    
                    return k
        
        return 1
        
