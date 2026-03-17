class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:

        edgeCount = defaultdict(int)

        for row in wall:
            pos = 0
            for brick in row[:-1]:
                pos+=brick
                edgeCount[pos]+=1
            
        
        max_edges = max(edgeCount.values(), default = 0)
        return len(wall) - max_edges


        
