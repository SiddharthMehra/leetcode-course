class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)

        def out_of_bounds(r, c):
            return r<0 or c<0 or r ==n or c==n
        

        def dfs(r,c, label):
            if (out_of_bounds(r,c) or grid[r][c]!=1):
                return 0
            
            grid[r][c] = label
            size = 1
            neighbor = [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]
            for nr, nc in neighbor:
                size+=dfs(nr, nc, label)
            
            return size

        #precompute areas
        size = defaultdict(int)
        label = 2
        for r in range(n):
            for c in range(n):
                if grid[r][c]:
                    size[label] = dfs(r,c,label)
                    label+=1
        
        def connect(r, c):
            neighbor = [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]
            visit = set()
            res = 1
            for nr, nc in neighbor:
                if not out_of_bounds(nr, nc) and grid[nr][nc] not in visit:
                    res+=size[grid[nr][nc]]
                    visit.add(grid[nr][nc])
            
            return res
        
        #try flipping water
        res = 0 if not size else max(size.values())
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    res = max(res, connect(r, c))
        
        return res

                
