class Solution:
    def maxFreqAtTarget(self, nums, target, k, maxOps):

        #count numbers already equal to target
        left = bisect_left(nums, target)
        right = bisect_right(nums, target)
        same = right - left

        #count numbers that can be converted to target
        lo = bisect_left(nums, target - k)
        hi = bisect_right(nums, target + k)
        convertible = hi - lo - same

        #we can only use max numOperations
        return same + min(maxOps, convertible)
    
    def maxFrequency(self, nums, k, numOperations):

        nums.sort()
        ans = 1

        for x in nums:
            ans = max(ans, 
            self.maxFreqAtTarget(nums, x, k, numOperations),
            self.maxFreqAtTarget(nums, x - k, k, numOperations),
            self.maxFreqAtTarget(nums, x + k, k, numOperations))
        
        return ans




            
