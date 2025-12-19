class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:

        pq = [(row[0], i, 0) for i, row in enumerate(nums)] #min of each sublit
        heapq.heapify(pq)

        ans = -1e9, 1e9
        right = max(row[0] for row in nums) # max of mins -> lowest possible max

        while pq:
            left, i, j = heapq.heappop(pq) #left, ith list, jth element
            if right - left<ans[1]-ans[0]:
                ans = left, right
            
            if j+1 == len(nums[i]): #reaching end of list
                return ans
            
            nxtValue = nums[i][j+1]
            right = max(right, nxtValue)
            heapq.heappush(pq, (nxtValue, i, j+1))
        

            




        
