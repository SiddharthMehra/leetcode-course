#binary search + BFS
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])

        def canReachDestination(mid):
            visited = [[False]*cols for _ in range(rows)]
            q = deque([(0, 0)])
            while q:
                x, y = q.popleft()
                if x == rows-1 and y == cols-1:
                    return True
                
                visited[x][y] = True
                for dx, dy in [[0,1],[1,0],[0,-1],[-1,0]]:
                    nx, ny = x+dx, y+dy
                    if 0<=nx<rows and 0<=ny<cols and not visited[nx][ny]:
                        current_diff = abs(heights[nx][ny] - heights[x][y])
                        if current_diff<=mid:
                            visited[nx][ny] = True
                            q.append((nx, ny))
        
        left, right = 0, 10**7

        while left<right:
            mid = (left+right)//2
            if canReachDestination(mid):
                right = mid
            else:
                left = mid+1
        
        return left
                        
