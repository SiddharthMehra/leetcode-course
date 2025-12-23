class Solution:
    def minDays(self, bloomDay, m, k):

        def canBloom(mid):
            num_of_bouquets, count = 0, 0
            for day in bloomDay:
                #if flower is bloomed, add to the set. else reset the count
                if day<=mid:
                    count+=1
                else:
                    count = 0
                
                if count == k:
                    num_of_bouquets+=1
                    count = 0
            
            return num_of_bouquets>=m
        
        #m bouquets of k flowers each
        if m*k>len(bloomDay):
            return -1
        
        start = 0
        end = max(bloomDay)
        minDays = -1

        while start<=end:
            mid = (start+end)//2
            #try to minimise the number of bloom days
            if canBloom(mid):
                minDays = mid
                end = mid-1
            else:
                start = mid+1
        
        return minDays
