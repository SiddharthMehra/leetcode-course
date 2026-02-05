class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:

        inc = dec = 0
        prev = 0 

        for i in range(len(nums)):
            d = target [i] - nums[i]

            if d>prev:
                inc+=d-prev
            else:
                dec+=prev-d
            
            prev = d
        
        return max(inc, dec)
        
