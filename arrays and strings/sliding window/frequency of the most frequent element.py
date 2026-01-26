
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        #sort + sliding window

        nums.sort()
        l, r = 0, 0
        res, total = 0, 0

        while r<len(nums):
            total+=nums[r]

            #while window is invalid, shrink the window
            while nums[r] * (r-l+1) > total + k:
                total-=nums[l]
                l+=1
            
            res = max(res, r-l+1)
            r+=1
        
        return res


