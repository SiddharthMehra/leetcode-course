class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        #always increment the smallest number
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
        
        while k:
            current = heapq.heappop(heap)
            heapq.heappush(heap, current+1)
            k-=1
        
        result = 1

        while len(heap)>0:
            x = heapq.heappop(heap)
            result = (result * x) %(10**9+7)
        
        return result
