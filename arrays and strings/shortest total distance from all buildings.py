class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        dist_matrix = [[0]* cols for row in range(rows)]

        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        BUILDING = 1
        OBSTACLE = 2    
        EMPTY_LAND = 0

        min_dist = float('inf')

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == BUILDING:
                    local_dist = float('inf')
                    q = deque([(row, col, 0)])

                    while q:
                        curr_row, curr_col, distance = q.popleft()

                        for dr, dc in directions:
                            next_row = curr_row + dr
                            next_col = curr_col + dc

                            if (0<=next_row<rows) and (0<=next_col<cols) and grid[next_row][next_col] == EMPTY_LAND:
                                grid[next_row][next_col]-=1
                                dist_matrix[next_row][next_col]+=distance+1
                                q.append((next_row, next_col, distance+1))
                                
                                local_dist = min(local_dist, dist_matrix[next_row][next_col])
                    
                    EMPTY_LAND-=1
                    min_dist = local_dist
            
        return min_dist if min_dist!=float('inf') else -1

        
        
