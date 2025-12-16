#multi source bfs
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)

        if rows == 0:
            return -1
        
        cols = len(grid[0])

        fresh_cnt = 0
        rotten = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    rotten.append((r,c))
                
                elif grid[r][c]==1:
                    fresh_cnt+=1
        
        minutes_passed = 0

        while rotten and fresh_cnt>0:
            minutes_passed+=1

            for _ in range(len(rotten)):
                x, y = rotten.popleft()

                for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nx, ny = x+dx, y+dy
                    #out of grid boundary
                    if nx<0 or nx==rows or ny<0 or ny == cols:
                        continue
                    #ignore the cell if is empty or visited before
                    if grid[nx][ny] == 0 or grid[nx][ny]==2:
                        continue

                    fresh_cnt-=1
                    grid[nx][ny] = 2 #mark current fresh orange as rotten
                    rotten.append((nx, ny))
    

        return minutes_passed if fresh_cnt == 0 else -1




        
