class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        n = len(grid)
        mid = n//2

        def isY(r, c):
            #upper left diagonal
            if r==c and r<=mid:
                return True
            
            #upper right diagonal
            if (r+c) == n-1 and r<=mid:
                return True
            
            #centre line downwards
            if c == mid and r>=mid:
                return True
            
            return False
        
        ans = float('inf')
        for a in range(3): #value for a
            for b in range(3): #value for b
                if a==b:
                    continue
                
                #a is part of Y, b is not
                operations = 0
                for r in range(n):
                    for c in range(n):
                        if isY(r, c):
                            if grid[r][c]!=a:
                                operations+=1
                        else:
                            if grid[r][c]!=b:
                                operations+=1
                
                ans = min(ans, operations)
        
        return ans
            

        
