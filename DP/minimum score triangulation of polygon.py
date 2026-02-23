class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:

        n = len(values)

        memo = [[-1] * n for _ in range(n)]

        def dp(i, j):

            #base case, less than 3 vertices
            if j-i<2:
                return 0
            
            if memo[i][j]!=-1:
                return memo[i][j]
            
            res = float('inf')

            #try all possible k between i and j

            for k in range(i+1, j):
                cost = dp(i, k) + dp(k, j) + values[i] * values[k] * values[j]
                res = min(res, cost)
            
            memo[i][j] = res
            return res
        
        return dp(0, n-1)
