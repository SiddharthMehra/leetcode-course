class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        
        n = len(prices)

        dps = [[[None] * 3 for _ in range(k+1)] for _ in range(n)]

        def dp(i, k, state):

            if i == n:
                return 0 if state == 0 else -inf
            
            if k == 0 and state!=0:
                return -inf
            
            if dps[i][k][state] is not None:
                return dps[i][k][state]
            
            #state 0: no position
            if state == 0:
                ans = max(dp(i+1, k, 0), #skip
                -prices[i] + dp(i+1, k, 1), #buy
                prices[i] + dp(i+1, k, 2) #short sell
                )
            
            #state 1: holding stock
            elif state == 1:
                ans = max(dp(i+1, k, 1), #hold
                prices[i] + dp(i+1, k-1, 0) #sell
                )
            
            #state 2: short position
            else:
                ans = max(dp(i+1, k, 2),
                -prices[i] + dp(i+1, k-1, 0))
            

            dps[i][k][state] = ans
        
            return ans
        
        return dp(0, k, 0)
