class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        stop_to_buses = defaultdict(list)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_buses[stop].append(i)
        
        visited_buses = set()
        q = deque()

        for bus in stop_to_buses[source]:
            q.append((bus, 1))
            visited_buses.add(bus)
        
        while q:
            bus, buses_taken = q.popleft()

            #if this buses reach target, we are done
            if target in routes[bus]:
                return buses_taken
            
            #explore neighboring buses
            for stop in routes[bus]:
                for next_bus in stop_to_buses[stop]:
                    if next_bus not in visited_buses:
                        visited_buses.add(next_bus)
                        q.append((next_bus, buses_taken+1))

        return -1
            



            

        




        
