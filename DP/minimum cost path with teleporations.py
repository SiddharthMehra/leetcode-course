class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:

        m, n = len(grid), len(grid[0])

        #sort all cells
        cells = [(i, j) for i in range(m) for j in range(n)]
        cells.sort(key = lambda p: grid[p[0]][p[1]])

        #costs[i][j] = minimum cost to reach bottom right from i,j
        costs = [[float('inf')] * n for _ in range(m)]

        for _ in range(k+1):
            min_so_far = float('inf')
            group_start = 0 #start value of equal value group

            i=0
            while i<len(cells):
                x,y = cells[i]
                min_so_far = min(min_so_far, costs[x][y])

                if (i+1)<len(cells) and grid[x][y] == grid[cells[i+1][0]][cells[i+1][1]]:
                    i+=1
                    continue
                
                for j in range(group_start, i+1):
                    r, c = cells[j]
                    costs[r][c] = min_so_far
                
                group_start = i+1
                i+=1
            
            #normal dp relaxation
            for r in range(m-1, -1, -1):
                for c in range(n-1, -1, -1):
                    if r == m-1 and c == n-1:
                        costs[r][c] = 0
                        continue
                    
                    if (r+1)<m:
                        costs[r][c] = min(costs[r][c], costs[r+1][c] + grid[r+1][c])
                    
                    if c+1<n:
                        costs[r][c] = min(costs[r][c], costs[r][c+1] + grid[r][c+1])
                    
        
        return costs[0][0]
