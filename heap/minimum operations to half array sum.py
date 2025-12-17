class Solution:
    def halveArray(self, nums: List[int]) -> int:

        half = sum(nums)/2

        heap  = [-num for num in nums]
        heapq.heapify(heap)
        operations = 0

        while half>0:
            largest = - heapq.heappop(heap)
            reduced = largest/2
            half-=reduced
            heapq.heappush(heap, -(largest-reduced) )
            operations+=1
        
        return operations


