class Solution: 
    def minTotalDistance(self, grid: List[List[int]]) -> int:

        rows, cols = [], []

        m, n = len(grid), len(grid[0])

        #collect rows, sorted because scanned row wise
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    rows.append(i)
        
        #collect cols sorted row wise
        for j in range(n):
            for i in range(m):
                if grid[i][j] == 1:
                    cols.append(j)
        
        row_median = rows[len(rows)//2]
        col_median = cols[len(cols)//2]

        #compute distance
        return sum(abs(r - row_median) for r in rows) + \
            sum(abs(c - col_median) for c in cols)
        
        


