class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:

        rows, cols = len(grid), len(grid[0])
        target = (rows-1, cols-1)

        if k>=rows+cols-2:
            return rows+cols-2
        
        state = (0, 0, k) #row, col, remaining quota
        q = deque([(0, state)]) # steps, state
        seen = set([state])

        while q:
            steps, (row, col, k) = q.popleft()

            if (row, col) == target:
                return steps
            
            for new_row, new_col in [(row, col+1), (row+1, col), (row-1, col), (row, col-1)]:
                if 0<=new_row<rows and 0<=new_col<cols:
                    new_eliminations = k-grid[new_row][new_col]

                    new_state = (new_row, new_col, new_eliminations)

                    if new_eliminations>=0 and new_state not in seen: #to ensure number of eliminations<=k
                        seen.add(new_state)
                        q.append((steps+1, new_state))
        
        return -1








