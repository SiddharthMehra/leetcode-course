class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        #if start or end is blocked
        if grid[0][0] == 1 or grid[m-1][n-1] == 1:
            return 0
        
        #initialise start with 1 way
        grid[0][0]=1

        #in the first row, you cannot come from above, only from left.
        for i in range(1, n):
            if grid[0][i] == 0 and grid[0][i-1] == 1:
                grid[0][i] = 1
            else:
                grid[0][i] = 0
        
        for j in range(1, m):
            if grid[j][0] == 0 and grid[j-1][0] == 1:
                grid[j][0] = 1
            else:
                grid[j][0] = 0
        
        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j]==1:
                    grid[i][j] = 0
                else:
                    grid[i][j] = grid[i-1][j] + grid[i][j-1]
        
        return grid[m-1][n-1]
        



