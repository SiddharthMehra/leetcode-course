class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:

        m, n = len(s1), len(s2)
        memo = {}

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            
            if i ==m: # s1 finished, remaining delete s2 characters
                memo[(i, j)] = sum(ord(c) for c in s2[j:])
                return memo[(i, j)]
            
            if j == n:
                memo[(i, j)] = sum(ord(c) for c in s1[i:])
                return memo[(i, j)]
            
            #if characters match, no deletion needed
            if s1[i] == s2[j]:
                memo[(i, j)] = dp(i+1, j+1)
            
            else:
                delete_s1 = ord(s1[i]) + dp(i+1, j)
                delete_s2 = ord(s2[j]) + dp(i, j+1)
                memo[(i, j)] = min(delete_s1, delete_s2)
            
            return memo[(i, j)]
        
        return dp(0, 0)
            

            

        
