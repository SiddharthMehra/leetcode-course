class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:

        nums.sort()
        n = len(nums)
        d = n//3

        i = n-2
        res = 0

        for _ in range(d):
            res+=nums[i]
            i-=2
        
        return res
        
