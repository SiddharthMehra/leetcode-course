class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0]*n
    
    def find(self, x):
        if self.parent[x]!=x:
            self.parent[x] = self.find(self.parent[x])
        
        return self.parent[x]
    
    def union(self, x, y):
        xset = self.find(x)
        yset = self.find(y)
        if xset == yset:
            return
        
        if self.rank[xset]>self.rank[yset]:
            self.parent[yset]=self.parent[xset]
            self.rank[xset]+=1
        
        else:
            self.parent[xset] = self.parent[yset]
            self.rank[yset]+=1

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        ds = DSU(n)

        for edge in edges:
            ds.union(edge[0], edge[1])
        
        parent = set()
        for i in range(n):
            parent.add(ds.find(i))
        
        return len(parent)
            
        
