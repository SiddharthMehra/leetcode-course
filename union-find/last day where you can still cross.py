class DSU:
    def __init__(self, n):
        self.root = list(range(n));
        self.rank = [1]*n

    def find(self, x):
        if self.root[x]!=x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)

        if rootx == rooty:
            return
        
        if self.rank[rootx]>self.rank[rooty]:
            self.rank[rootx]+=self.rank[rooty]
            self.root[rooty] = rootx
        else:
            self.rank[rooty]+=self.rank[rootx]
            self.root[rootx] = rooty

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        dsu = DSU(row*col+2)
        grid = [[1] * col for _ in range(row)]
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        #virtual nodes added to the top and bottom
        #iterate in reverse, flooded to land
        for i in range(len(cells)-1, -1, -1):
            r, c = cells[i][0]-1, cells[i][1]-1
            grid[r][c]=0
            index_1 = r*col + c +1
            for dr, dc in directions:
                new_r, new_c = r+dr, c+dc
                index_2 = new_r*col + new_c+1
                if 0<=new_r<row and 0<=new_c<col and grid[new_r][new_c] == 0:
                    dsu.union(index_1, index_2)
            
            if r==0:
                dsu.union(0, index_1)
            
            if r==row-1:
                dsu.union(row*col+1, index_1)
            
            if dsu.find(0) == dsu.find(row*col+1):
                return i



        
