class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        m, n = len(s1), len(s2)
        memo = {}
        
        def dp(i, j):

            if (i, j) in memo:
                return memo[(i, j)]
            
            k = i+j
            if k == len(s3):
                return True
            
            ans = False
            if i<m and s1[i] == s3[k]:
                ans = dp(i+1, j)
            
            if not ans and j<n and s2[j] == s3[k]:
                ans = dp(i, j+1)
            
            memo[(i, j)] = ans
            return ans
        
        return dp(0, 0)
