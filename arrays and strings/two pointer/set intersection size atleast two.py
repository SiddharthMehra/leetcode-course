class Solution:
    def intersectionSizeTwo(self, nums:List[int])->int:
        res = 0
        nums.sort( key = lambda x : (x[1], -x[0]))

        p1, p2 = -1, -1
        ans=0
        for s,e in nums:
            #already have two points
            if s<=p1:
                continue
            
            #only 1 point, add 1 more
            elif s<=p2:
                ans+=1
                p1 = p2
                p2 = e
            
            else:
                ans+=2
                p1 = e-1
                p2 = e
        
        return ans
            

