class Solution:
    def convertArray(self, nums: List[int]) -> int:

        def solve(arr):
            heap = []
            cost = 0

            for num in arr:
                #max heap
                heapq.heappush(heap, -num)

                #if order violated, make top equal to num
                if -heap[0]>num:
                    top=-heapq.heappop(heap)
                    cost+=top-num
                    heapq.heappush(heap, -num)
            
            return cost

        
        #non decreasing
        cost1 = solve(nums)
        #non increasing
        cost2 = solve(nums[::-1])

        return min(cost1, cost2)
