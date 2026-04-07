class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:

        n = len(grid)
        pos = [-1] * n
        #find last '1'
        for i in range(n):
            for j in range(n-1, -1, -1):
                if grid[i][j] == 1:
                    pos[i] = j
                    break
        
        ans = 0
        #swap j and i if pos[j]<=i
        for i in range(n):
            k=-1
            for j in range(i, n):
                if pos[j]<=i:
                    ans+=j-i
                    k = j
                    break

            #bubble up k to i
            if k!=-1:
                for j in range(k, i, -1):
                    pos[j], pos[j-1] = pos[j-1], pos[j]
            
            else:
                return -1
        
        return ans

        
