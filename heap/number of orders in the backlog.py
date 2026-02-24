import heapq

class Solution:
    def getNumberOfBacklogOrders(self, orders):
        MOD = 10**9 + 7
        
        # Max heap for buy orders (store negative price for max heap)
        buy_heap = []
        
        # Min heap for sell orders
        sell_heap = []
        
        for price, amount, orderType in orders:
            
            if orderType == 0:  # Buy order
                # Match with lowest sell price
                while amount > 0 and sell_heap and sell_heap[0][0] <= price:
                    sell_price, sell_amount = heapq.heappop(sell_heap)
                    
                    if sell_amount > amount:
                        heapq.heappush(sell_heap, (sell_price, sell_amount - amount))
                        amount = 0
                    else:
                        amount -= sell_amount
                
                if amount > 0:
                    heapq.heappush(buy_heap, (-price, amount))
            
            else:  # Sell order
                # Match with highest buy price
                while amount > 0 and buy_heap and -buy_heap[0][0] >= price:
                    buy_price, buy_amount = heapq.heappop(buy_heap)
                    
                    if buy_amount > amount:
                        heapq.heappush(buy_heap, (buy_price, buy_amount - amount))
                        amount = 0
                    else:
                        amount -= buy_amount
                
                if amount > 0:
                    heapq.heappush(sell_heap, (price, amount))
        
        # Count remaining backlog
        total = 0
        for _, amount in buy_heap:
            total = (total + amount) % MOD
        for _, amount in sell_heap:
            total = (total + amount) % MOD
        
        return total
