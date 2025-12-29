#lcs variation -> iterate from right to left to prevent crossing of lines

class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        memo = {}

        def dp(i, j):
            if i<0 or j<0:
                return 0
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            if nums1[i] == nums2[j]:
                memo[(i, j)] = 1 + dp(i-1, j-1)
            else:
                memo[(i, j)] = max(dp(i-1, j), dp(i, j-1))
            
            return memo[(i, j)]
        
        return dp(m-1, n-1)
