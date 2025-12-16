class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:    
        m, n = len(grid), len(grid[0])
        q = deque()

        #left and right boundary
        for i in range(m):
            if grid[i][0]==1:
                q.append((i, 0))
            if grid[i][n-1]==1:
                q.append((i, n-1))
        
        #upper and bottom boundary
        for j in range(n):
            if grid[0][j]==1:
                q.append((0, j))
        
            if grid[m-1][j]==1:
                q.append((m-1, j))

        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        while q:
            r,c = q.popleft()
            if grid[r][c]==0:
                continue
            
            grid[r][c] = 0 #sink the land

            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if 0<=nr<m and 0<=nc<n and grid[nr][nc]==1:
                    q.append((nr, nc))
        
        return sum(grid[r][c] for r in range(m) for c in range(n))
