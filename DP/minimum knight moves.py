class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:

        memo = {}

        def dfs(x, y):
            x, y = abs(x), abs(y)

            if (x,y) in memo:
                return memo[(x, y)]
            
            if x+y == 0:
                return 0
            
            if x+y==2:
                return 2
            
            result = min(dfs(x-1, y-2), dfs(x-2, y-1)) + 1
            memo[(x, y)] = result
            return result
        
        return dfs(x, y)
