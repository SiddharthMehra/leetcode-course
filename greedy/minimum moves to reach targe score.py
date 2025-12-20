class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        ans = 0
        while target>1 and maxDoubles>0:
            if target%2==0:
                ans+=1
                target//=2
                maxDoubles-=1
            else:
                target-=1
                ans+=1
        if target>1:
            ans+=target-1
        
        return ans




        
