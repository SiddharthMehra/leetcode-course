class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        start_row, start_col = entrance
        seen = {(start_row, start_col)}

        q = deque()
        q.append([start_row, start_col, 0]) #row, col, steps

        while q:
            r,c, distance = q.popleft()
            for dr, dc in directions:
                next_row, next_col = r+dr, c+dc
                if 0<=next_row<rows and 0<=next_col<cols and maze[next_row][next_col] == "." and (next_row, next_col) not in seen:
                    #if this empty cell is an exit, return distance+1
                    if 0==next_row or next_row == rows-1 or 0==next_col or next_col == cols-1:
                        return distance+1
                    
                    seen.add((next_row, next_col))
                    q.append([next_row, next_col, distance+1])
        
        return -1
