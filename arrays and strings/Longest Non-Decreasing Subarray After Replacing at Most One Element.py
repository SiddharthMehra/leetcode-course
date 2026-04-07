class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        n = len(nums)
        left, right = [1] * n, [1] * n

        for i in range(1, n):
            if nums[i-1]<=nums[i]:
                left[i] = left[i-1] + 1
        
        #right to left
        for i in range(n-2, -1, -1):
            if nums[i]<=nums[i+1]:
                right[i] = right[i+1] + 1
        
        res = min(n, max(left) + 1)

        #try connecting left with right and replacing element at i
        for i in range(1, n-1):
            if nums[i-1]<=nums[i+1]:
                res = max(res, left[i-1] + 1 +right[i+1])
        
        return res
        
