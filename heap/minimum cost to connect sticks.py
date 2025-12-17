class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        minHeap = sticks
        heapify(minHeap)
        cost = 0

        while len(minHeap)>1:
            new_stick = heappop(minHeap) + heappop(minHeap)
            cost+=new_stick
            heappush(minHeap, new_stick)
        
        return cost
            
        
