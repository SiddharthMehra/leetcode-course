class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:

        nums.sort()

        prev = -10 ** 18
        count = 0

        for x in nums:
            candidate = max(prev+1, x-k)
            if candidate<=x+k:
                count+=1
                prev = candidate
            
        
        return count
        
