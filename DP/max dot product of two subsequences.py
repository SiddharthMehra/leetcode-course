class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        
        memo = {}
        def dp(i, j):
            if i == len(nums1) or j == len(nums2):
                return 0
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            take = nums1[i] * nums2[j] + dp(i+1, j+1)
            skip1 = dp(i+1, j)
            skip2 = dp(i, j+1)

            memo[(i, j)] = max(take,skip1, skip2)
            return memo[(i, j)]
        
        if max(nums1)<0 and min(nums2)>0:
            return max(nums1) * min(nums2)
        
        if min(nums1)>0 and max(nums2)<0:
            return min(nums1) * max(nums2)
        
        return dp(0, 0)
            

