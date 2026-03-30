class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:

        if len(sentence1)!=len(sentence2):
            return False
        
        parent = {}
        rank = {}

        def find(x):
            if x not in parent:
                parent[x] = x
                rank[x] = 0
            
            if parent[x]!=x:
                parent[x] = find(parent[x])
            
            return parent[x]
        
        #union by rank
        def union(x, y):
            rootX = find(x)
            rootY = find(y)

            if rootX == rootY:
                return
            
            if rank[rootX]>rank[rootY]:
                parent[rootY] = rootX
            
            elif rank[rootX]<rank[rootY]:
                parent[rootX] = rootY
            
            else:
                parent[rootY] = rootX
                rank[rootX]+=1
            
        
        #build DSU
        for a,b in similarPairs:
            union(a, b)
        
        for a,b in zip(sentence1, sentence2):
            if find(a)!=find(b):
                return False
        
        return True
