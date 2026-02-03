class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        max_heap = []

        fuel = startFuel
        prev_pos = 0
        stops = 0

        stations.append([target, 0])

        for pos, gas in stations:

            #fuel needed to reach this position
            fuel -= (pos - prev_pos)

            #refuel from past max
            while fuel<0 and max_heap:
                fuel+=-heapq.heappop(max_heap)
                stops+=1
            
            #still negative, cannot reach this location
            if fuel<0:
                return -1
            
            #now reachable, store its fuel
            heapq.heappush(max_heap, -gas)
            prev_pos = pos
        
        return stops

