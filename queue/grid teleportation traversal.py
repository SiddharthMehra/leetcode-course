class Solution:
    def minMoves(self, matrix: List[str]) -> int:

        if not matrix:
            return -1
        
        m, n = len(matrix), len(matrix[0])

        #if start or end is blocked
        if matrix[0][0] == '#' or matrix[m-1][n-1] == '#':
            return -1
        
        #build portal map
        portals = defaultdict(list)
        for r in range(m):
            for c in range(n):
                if matrix[r][c].isalpha():
                    portals[matrix[r][c]].append((r,c))
        
        #step 2 bfs
        queue = deque([(0, 0, 0)]) #row, col, dist
        visited = [[False] * n for _ in range(m)]
        visited[0][0] = True

        used_portals = set()

        while queue:
            r, c, dist = queue.popleft()

            if r == m-1 and c == n-1:
                return dist
            
            for dr, dc in [(1,0),(-1,0),(0,1), (0,-1)]:
                nr, nc = r+dr, c+dc
                if 0<=nr<m and 0<=nc<n:
                    if not visited[nr][nc] and matrix[nr][nc]!='#':
                        visited[nr][nc] = True
                        queue.append((nr, nc, dist+1))
            
            #teleportation
            cell_value = matrix[r][c]
            if cell_value.isalpha() and cell_value not in used_portals:
                for nr, nc in portals[cell_value]:
                    visited[nr][nc] = True
                    queue.appendleft((nr, nc, dist)) #no move, teleport therefore appendleft
                
                used_portals.add(cell_value)
            
        return -1

        
