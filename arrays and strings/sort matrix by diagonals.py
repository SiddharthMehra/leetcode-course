class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:

        diagonals = defaultdict(list)
        n = len(grid)

        #group elements
        for r in range(n):
            for c in range(n):
                diagonals[r-c].append(grid[r][c])
            
        #sort each diagonal
        for d in diagonals:
            if d>=0:
                diagonals[d].sort(reverse = True)
            else:
                diagonals[d].sort()
        
        #write back
        for r in range(n):
            for c in range(n):
                d = r - c
                grid[r][c] = diagonals[d].pop(0)
        
        return grid


        
