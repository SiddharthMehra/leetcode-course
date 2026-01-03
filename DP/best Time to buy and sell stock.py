class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        #find the minimum price at any given point of time and subtract the current price
        for i in range(len(prices)):
            if prices[i]<min_price:
                min_price = prices[i]
            max_profit = max(max_profit, prices[i] - min_price)
        
        return max_profit
