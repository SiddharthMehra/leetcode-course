class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-pile for pile in piles]
        heapq.heapify(piles)
        
        for _ in range(k):
            curr = -heapq.heappop(piles)
            remove = curr//2
            heapq.heappush(piles, -(curr-remove))
            
        return -sum(piles)
        
        
