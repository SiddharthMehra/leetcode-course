class Solution:
    def distanceToCycle(self, n: int, edges: List[List[int]]) -> List[int]:
        
        #topological sort + multi source bfs
        graph = defaultdict(list)
        degree = [0] * n

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u]+=1
            degree[v]+=1
        
        q = deque()
        #remove leaves
        for i in range(n):
            if degree[i] == 1:
                q.append(i)
        
        removed = [False] * n

        while q:
            node = q.popleft()
            removed[node] = True

            for nei in graph[node]:
                degree[nei]-=1
                if degree[nei] == 1:
                    q.append(nei)
        
        #cycle nodes have distance 0 to the cycle obviously
        dist = [-1] * n
        q = deque()

        for i in range(n):
            if not removed[i]:
                dist[i] = 0
                q.append(i)
        
        #bfs outward from the cycle nodes

        while q:
            node = q.popleft()

            for nei in graph[node]:
                if dist[nei] == -1:
                    dist[nei] = dist[node]+1
                    q.append(nei)
            
        return dist
        
