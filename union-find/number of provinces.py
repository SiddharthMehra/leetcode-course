class UnionFind:

    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0]*size
    
    def find(self, x):
        if self.parent[x]!=x:
            self.parent[x] = self.find(self.parent[x])
        
        return self.parent[x]
    
    def union(self, x, y):
        xset = self.find(x)
        yset = self.find(y)

        if self.rank[xset]>self.rank[yset]:
            self.parent[yset] = self.parent[xset]
            self.rank[xset]+=1
        else:
            self.parent[xset] = self.parent[yset]
            self.rank[yset]+=1

class Solution:

    def findCircleNum(self, isConnected: List[List[int]]):

        n  = len(isConnected)
        uf = UnionFind(n)
        numberOfComponents = n

        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j]==1 and uf.find(i)!=uf.find(j):
                    numberOfComponents-=1
                    uf.union(i, j)
        
        return numberOfComponents
    
        
