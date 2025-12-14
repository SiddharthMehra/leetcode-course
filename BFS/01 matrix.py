class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        q = deque()
        seen = set()

        def valid(row, col):
            return 0<=row<m and 0<=col<n

        #prepare q initally with all 0 cells
        for row in range(m):
            for col in range(n):
                if matrix[row][col]==0:
                    q.append((row, col, 0))
                    seen.add((row, col))
        
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        while q:
            row, col, steps = q.popleft()

            for dx, dy in directions:
                next_row, next_col = row+dx, col+dy
                if (next_row, next_col) not in seen and valid(next_row, next_col):
                    seen.add((next_row, next_col))
                    q.append((next_row, next_col, steps+1))

                    maxtrix[next_row][next_col] = steps+1
        
        return matrix




