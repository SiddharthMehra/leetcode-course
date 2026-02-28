class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        if not matrix:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]

        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        def dfs(r, c):
            if dp[r][c]!=0:
                return dp[r][c]
            
            max_length = 1

            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if 0<=nr<m and 0<=nc<n:
                    if matrix[nr][nc]>matrix[r][c]:
                        length = 1 + dfs(nr, nc)
                        max_length = max(max_length, length)
                    
            dp[r][c] = max_length
            return max_length
        
        answer = 0
        for i in range(m):
            for j in range(n):
                answer = max(answer, dfs(i, j))
        
        return answer
            
