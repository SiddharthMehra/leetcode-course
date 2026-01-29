class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:

        events_start = sorted(events, key = lambda x: x[0])
        events_end = sorted(events, key = lambda x: x[1])

        ans, best = 0, 0
        j = 0
        n = len(events)

        for s,e,v in events_start:
            #compare all eventss that ended before the current start time
            while j<n and events_end[j][1]<s:
                best = max(best, events_end[j][2])
                j+=1
            
            #pick either the current or  2 events
            ans = max(ans, v, best + v)
        
        return ans

        
