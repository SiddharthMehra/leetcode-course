class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:

        n = len(events)
        #max end day
        max_day = max(event[1] for event in events)
        #to process events in order, first sort bu start time and then end time
        events.sort()
        pq = []
        ans, j = 0, 0

        for i in range(1, max_day+1):
            #if event start time is less than current time, push end time to the heap
            while j<n and events[j][0]<=i:
                heapq.heappush(pq, events[j][1])
                j+=1
            
            #remove events from the heap who have ended before the current time
            while pq and pq[0]<i:
                heapq.heappop(pq)
            
            #element with the least end time is popped out to push maximum events eventually
            if pq:
                heapq.heappop(pq)
                ans+=1
        
        return ans
            
