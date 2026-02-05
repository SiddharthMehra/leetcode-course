class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:

        def find(x):
            while x in parent:
                if parent[x] in parent:
                    parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(x, y):
            rootx, rooty = find(x), find(y)
            if rootx == rooty:
                return False
            parent[rootx] = rooty
            return True
        
        seen, parent, res, count = set(), {}, [], 0

        for x, y in positions:
            if (x,y) not in seen:
                seen.add((x, y))
                count+=1

                for i, j in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                    if (i, j) in seen and union((i, j), (x, y)):
                        count-=1
            
            res.append(count)
        
        return res
        
