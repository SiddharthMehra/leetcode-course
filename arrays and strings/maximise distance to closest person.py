class Solution(object):
    def maxDistToClosest(self, seats):

        n = len(seats)
        prev = -1
        max_dist = 0

        for i in range(n):
            if seats[i]==1:
                if prev == -1:
                    max_dist = i
                
                else:
                    #person sits exactly middle between i and prev
                    max_dist = max(max_dist, (i-prev)//2)
                
                prev = i
        
        #check distance from last position 
        max_dist = max(max_dist, n - 1 - prev)
        return max_dist
            
