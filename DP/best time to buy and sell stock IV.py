class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        if not prices or k==0:
            return 0
        
        #unlimited transactions, compare prev and compare and take profit if positive
        if k*2>=n:
            res = 0
            for i, j in zip(prices[1:], prices[:-1]):
                res+=max(0, i-j)
            
            return res
        
        #dp[i][j][k] = index, transactions executed, boolean holding
        dp = [[[-math.inf]*2 for _ in range(k+1)] for _ in range(n)]

        dp[0][0][0] = 0
        #buy on first day
        dp[0][1][1] = -prices[0]

        for i in range(1,n):
            for j in range(k+1):
                #if you are not holding, either remain not holding or sell today
                #sell does not consumer transaction, we count it during buy
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])


                #if holding keep holding or buy today
                #buy consumes transaction
                if j>0:
                    dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])
        
        #at the end it should be not holding
        res = max(dp[n-1][j][0] for j in range(k+1))
        return res
