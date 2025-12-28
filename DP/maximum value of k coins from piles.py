class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        dp = [[-1]*(k+1) for _ in range(n)]

        def dfs(i, coins):

            if i==n:
                return 0
            
            if dp[i][coins]!=-1:
                return dp[i][coins]
            
            #skip
            dp[i][coins] = dfs(i+1, coins)
            currPile = 0

            #take coins from ith pile from 0-j where j is min(coins) and len(piles[i])
            for j in range(min(coins, len(piles[i]))):
                currPile+=piles[i][j]
                dp[i][coins] = max(dp[i][coins], currPile + dfs(i+1, coins-j-1))
        
            return dp[i][coins]
        
        return dfs(0, k)

