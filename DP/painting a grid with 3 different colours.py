class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:

        def getColor(mask, pos):
            return (mask >> (2*pos)) & 3
        
        def setColor(mask, pos, color):
            return mask | (color<<(2*pos))
        
        MOD = 10**9+7
        
        def dfs(r, currColMask, prevColMask, out):
            if r == m:
                out.append(currColMask)
                return
            
            for i in [1,2,3]: # i in [1=RED, 2 = GREEN, 3 = BLUE]
                if getColor(prevColMask, r)!=i and (r==0 or getColor(currColMask, r-1)!=i):
                    dfs(r+1, setColor(currColMask, r, i), prevColMask, out)
        
        @lru_cache(None)
        def neighbor(prevColMask):
            out = []
            dfs(0, 0, prevColMask, out)
            return out
        
        @lru_cache(None)
        def dp(c, prevColMask):
            if c == n:
                return 1
            
            ans = 0
            for nei in neighbor(prevColMask):
                ans = (ans + dp(c+1, nei)) % MOD
            
            return ans
        
        return dp(0, 0)


        
