#expand around centre

class Solution:
    def countSubstrings(self, s: str) -> int:

        n = len(s)
        ans = 0
        
        def expand(i, j):
            nonlocal ans

            while i>=0 and j<n and s[i] == s[j]:
                ans+=1
                i-=1
                j+=1
            
        for k in range(n):
            expand(k, k)
            expand(k, k+1)
            
        return ans


        
