class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:

        arrival = [dist[i]/speed[i] for i in range(len(dist))]
        arrival.sort()

        #greedy elimination
        for minute in range(len(arrival)):
            if arrival[minute]<=minute:
                return minute
        
        return len(arrival)
