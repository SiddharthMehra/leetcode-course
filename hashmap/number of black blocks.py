class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        block_count = defaultdict(int)

        for x,y in coordinates:
            for dx in [0, -1]:
                for dy in [0, -1]:
                    nx, ny = x+dx, y+dy
                    if 0<=nx<m-1 and 0<=ny<n-1:
                        block_count[(nx, ny)]+=1

        res = [0]*5
        for count in block_count.values():
            res[count]+=1
        
        total_blocks = (m-1) * (n-1)
        #box with 0 black cells = total blocks - all blocks with 1 or more black cells
        res[0] = total_blocks - sum(res[1:])

        return res
        
