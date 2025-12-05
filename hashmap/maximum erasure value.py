class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        res = 0
        curr_sum, start = 0, 0
        seen = set()

        for end in range(len(nums)):
            while nums[end] in seen:
                seen.remove(nums[start])
                curr_sum-=nums[start]
                start+=1
            
            curr_sum+=nums[end]
            seen.add(nums[end])

            res = max(res, curr_sum)
        
        return res
    


        