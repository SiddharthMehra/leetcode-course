class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        hold, free = -prices[0], 0

        for i in range(1, n):
            tmp = hold

            #max of either previous hold and didnt hold previously and now buying
            hold = max(hold, free - prices[i])

            #max of either didnt hold previously and holding previously and now selling
            free = max(free, tmp + prices[i] - fee)
        
        return free
            
