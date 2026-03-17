class Solution:
    def maxTransactions(self, transactions: List[int]) -> int:

        heap = []
        balance = 0

        for t in transactions:
            balance+=t
            heapq.heappush(heap, t)

            #if balance<0, just remove the maximum negative transaction for largest effect
            if balance<0:
                removed = heapq.heappop(heap)
                balance-=removed
        
        return len(heap)
        
