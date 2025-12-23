class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        INF = 10**9
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]

        fire_time = [[INF] * n for _ in range(m)]
        q = deque()

        for i in range(m):
            for j in range(n):
                #fire source
                if grid[i][j]==1:
                    fire_time[i][j]=0
                    q.append((i, j))
                #wall, fire cannot pass through
                elif grid[i][j]==2:
                    fire_time[i][j]=-1
        
        while q:
            i, j = q.popleft()
            for dr, dc in dirs:
                nx, ny = i+dr, j+dc
                if 0<=nx<m and 0<=ny<n:
                    #fire up nx, ny
                    if fire_time[nx][ny] == INF:
                        fire_time[nx][ny] = fire_time[i][j]+1
                        q.append((nx, ny))
        
        fire_time[m-1][n-1]+=1

        def can_escape(wait):
            if wait >= fire_time[0][0]:
                return False
            visited = [[INF]*n for _ in range(m)]
            #you start at wait -> (i, j, time to start)
            q = deque([(0, 0, wait)])
            visited[0][0] = wait

            while q:
                i, j, time = q.popleft()
                if (i, j) == (m-1, n-1):
                    return True
                
                for di, dj in dirs:
                    ni, nj = i+di, j+dj
                    if 0<=ni<m and 0<=nj<n:
                        if fire_time[ni][nj]!=-1: #ni, nj = -1 for wall
                            next_time = time+1
                            #visit before fire and do not count if you visit at different time
                            if next_time<fire_time[ni][nj] and next_time<visited[ni][nj]:
                                visited[ni][nj] = next_time
                                q.append((ni, nj, next_time))
            
            return False
        
        left, right = 0, 10**9
        ans = -1

        # If you can't escape even immediately, answer is -1
        if not can_escape(0):
            return -1

        # If fire never reaches destination, you can wait forever
        if fire_time[m-1][n-1] >= INF:
            return 10**9

        while left<=right:
            mid = (left+right)//2
            #try to increase time
            if can_escape(mid):
                ans = mid
                left = mid+1
            else:
                right = mid-1
        
        return ans

        

        
