class Solution:
    def maxSum(self, nums: List[int]) -> int:
        
        #if all negative, just return the max element
        if all(n<0 for n in nums):
            return max(nums)
        
        #otherwise, just return the sum of only positive elements
        unique = set(nums)
        return sum(n for n in unique if n>0)
        
