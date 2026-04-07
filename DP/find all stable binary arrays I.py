mod = 10**9+7
class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        memo = {}

        def dp(z, o, last, cnt):

            if (z, o, last, cnt) in memo:
                return memo[(z, o, last, cnt)]
            
            if z == 0 and o == 0:
                return 1
            
            res = 0

            #try placing zero
            if z>0:
                if last == 0:
                    if cnt<limit:
                        res+=dp(z-1, o, 0, cnt+1)
                    
                else:
                    res+=dp(z-1, o, 0, 1)
            
            #try placing one
            if o>0:
                if last == 1:
                    if cnt<limit:
                        res+=dp(z, o-1, 1, cnt+1)
                
                else:
                    res+=dp(z, o-1, 1, 1)
            
            res%=mod
            memo[(z, o, last, cnt)] = res
            return res
        
        return dp(zero, one, -1, 0)

            


        
