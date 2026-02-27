class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:

        mod = 10**9+7
        m, n = len(grid), len(grid[0])

        # -1 means not computed
        memo = [[[-1] * k for _ in range(n)] for _ in range(m)]

        def dfs(i, j, remainder):
            if i>=m or j>=n:
                return 0
            
            if memo[i][j][remainder]!=-1:
                return memo[i][j][remainder]
            
            if i == m-1 and j == n-1:
                return 1 if remainder % k == 0 else 0
            
            total = 0

            #move down
            if i+1<m:
                new_rem = (remainder + grid[i+1][j]) % k
                total+=dfs(i+1, j, new_rem)
            
            #moe right
            if j+1<n:
                new_rem = (remainder + grid[i][j+1]) % k
                total+=dfs(i, j+1, new_rem)
            
            memo[i][j][remainder]= total % mod
            return memo[i][j][remainder]
        
        return dfs(0, 0, grid[0][0] % k)
        
