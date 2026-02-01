from functools import lru_cache

#instead of going backwards and forwards, simulate twice going forward. collect only cherry even if both reach the same cell
class Solution(object):
    def cherryPickup(self, grid):

        n = len(grid)

        memo =[[[None] * n for _ in range(n)] for _ in range(n)]

        #r1 + c1 = r2 + c2 since both of them are moving forward
        def dp(r1, c1, r2):
            
            #cherry collected at the final cell
            if r1 == n - 1 and c1 == n - 1:
                return grid[r1][c1]

            c2 = r1+ c1 - r2

            #out of bounds
            if r1>=n or r2>=n or c1>=n or c2>=n:
                return float('-inf')
            
            #thorn
            if grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return float('-inf')
            
            if memo[r1][c1][r2] is not None:
                return memo[r1][c1][r2]
            
            cherries = grid[r1][c1]
            if r1!=r2 or c1!=c2:
                cherries+=grid[r2][c2]
            
            best_next = max(
    dp(r1 + 1, c1, r2 + 1),  # down, down
    dp(r1, c1 + 1, r2),      # right, right
    dp(r1 + 1, c1, r2),      # down, right
    dp(r1, c1 + 1, r2 + 1),  # right, down ✅
)


            memo[r1][c1][r2] = cherries + best_next
            return memo[r1][c1][r2]

        return max(0, dp(0, 0, 0))

