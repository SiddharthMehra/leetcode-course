class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        mp = defaultdict(list)
        for width, height in rectangles:
            mp[height].append(width)
        #sort by width
        for v in mp.values():
            v.sort()
        
        ans=[]
        max_height = max(mp.keys())
        for x,y in points:
            cnt = 0
            #height range max 101 greater than current height y
            for height in range(y, max_height+1):
                if height in mp:
                    #count rectangles with width greater than 
                    cnt+=len(mp[height]) - bisect_left(mp[height], x)
            ans.append(cnt)
        
        return ans
