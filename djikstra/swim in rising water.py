class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visit = set()
        minHeap = [[grid[0][0], 0, 0]]
        visit.add((0,0))
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        while minHeap:
            t, r, c = heappop(minHeap)
            visit.add((r,c))

            if (r,c) == (n-1, n-1):
                return t
            
            for dr, dc in directions:
                nx, ny = r+dr, c+dc
                if nx<0 or nx>=n or ny<0 or ny>=n or (nx, ny) in visit:
                    continue

                visit.add((nx, ny))
                heappush(minHeap, [max(t, grid[nx][ny]), nx, ny])

        
