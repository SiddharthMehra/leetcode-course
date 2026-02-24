class Solution:
    def countSubarrays(self, nums: List[int]) -> int:

        curr = res = 1
        n = len(nums)

        for i in range(1, n):
            if nums[i]<=nums[i-1]:
                curr = 1
            
            else:
                curr+=1
            res+=curr
        
        return res
