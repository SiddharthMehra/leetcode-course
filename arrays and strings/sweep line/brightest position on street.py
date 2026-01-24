class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        #sweep line

        d = defaultdict(int)

        #mark in and out of range of lights
        for i, dis in lights:

            d[i-dis]+=1
            d[i+dis+1]-=1
        
        curr, position, max_val = 0, -1, -sys.maxsize

        #go in ascending order of position
        for idx, val in sorted(d.items()):
            curr+=val
            if curr>max_val:
                max_val, position = curr, idx
        
        return position 



