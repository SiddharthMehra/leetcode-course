from bisect import bisect_right, insort
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        ans = [-1] * n
        last_full_day = {}
        dry_day_indices = []

        for day, lake in enumerate(rains):
            if lake == 0:
                #dry day, store in sorted order
                insort(dry_day_indices, day)
                ans[day] = 1 #temporary value
            else:
                ans[day] = -1
                if lake in last_full_day:
                    last_rain_day = last_full_day[lake]
                    #find earliest dry day after the lake became full
                    idx = bisect_right(dry_day_indices, last_full_day[lake])
                    #no dry day, flood
                    if idx == len(dry_day_indices):
                        return []
                    
                    #assign the lake to dry
                    dry_day_to_use = dry_day_indices[idx]
                    ans[dry_day_to_use] = lake
                    #remove the dry day from sorted list
                    dry_day_indices.pop(idx)
                #update the last full day for lake
                last_full_day[lake] = day
            
        return ans
                    

        
