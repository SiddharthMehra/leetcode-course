class Solution:
     def findCheapestPrice(self, n, flights, src, dst, k):
        adj = [[] for _ in range(n)]
        for source, destination, price in flights:
            adj[source].append((destination, price))
        
        #(stops, node, dist)
        q = deque([(0, src, 0)])

        dist = [math.inf]*n
        dist[src] = 0

        while q:
            stops, node, cost = q.popleft()

            if stops>k:
                continue
            
            for neighbor, price in adj[node]:
                if cost + price < dist[neighbor] and stops<=k:
                    dist[neighbor] = cost+price
                    q.append([stops+1, neighbor, cost + price])
        
        return -1 if dist[dst] == math.inf else dist[dst]
