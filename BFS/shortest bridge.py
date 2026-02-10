from collections import deque

class Solution:
    def shortestBridge(self, grid):

        n = len(grid)

        directions = [(0,1),(1,0),(-1,0),(0, -1)]
        visit=set()

        def invalid(r, c):
            return r<0 or c<0 or r==n or c==n
        
        #visit first island
        def dfs(r, c):
            if (invalid(r,c) or not grid[r][c] or (r, c) in visit):
                return
            visit.add((r,c ))
            for dr, dc in directions:
                dfs(r+dr, c+dc)
        
        #shortest path to second island
        def bfs():
            res = 0
            q = deque(visit)
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in directions:
                        currR, currC = r+dr, c+dc
                        if invalid(currR, currC) or (currR, currC) in visit:
                            continue
                        #reached land
                        if grid[currR][currC]:
                            return res
                        
                        q.append([currR, currC])
                        visit.add((currR, currC))
                res+=1
            
        
        for r in range(n):
            for c in range(n):
                if grid[r][c]:
                    dfs(r, c)
                    return bfs()



