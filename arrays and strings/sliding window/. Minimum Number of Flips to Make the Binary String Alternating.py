class Solution:
    def minFlips(self, s: str) -> int:

        n = len(s)
        s = s + s

        diff0 = diff1 = 0
        res = float('inf')
        left = 0

        for right in range(2*n):
            exp0 = '0' if right%2==0 else '1'
            exp1 = '1' if right%2==0 else '0'
        
            if s[right]!=exp0:
                diff0+=1
            if s[right]!=exp1:
                diff1+=1
            
            if (right-left+1)>n:
                exp0 = '0' if left%2 == 0 else '1'
                exp1 = '1' if left%2==0 else '0'

                if s[left]!=exp0:
                    diff0-=1
                if s[left]!=exp1:
                    diff1-=1
                
                left+=1
            
            if right-left+1 == n:
                res = min(res, diff0, diff1)
            
        
        return res
        
