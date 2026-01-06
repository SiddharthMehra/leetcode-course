class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        n = len(coins)
        if n == 1:
            return 0
        
        graph = [[] for _ in range(n)]
        degree = [0] * n

        #undirected graph
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u]+=1
            degree[v]+=1
        
        #remove leaf nodes with no coin
        q = deque()
        for i in range(n):
            if degree[i] == 1 and coins[i] == 0:
                q.append(i)
        
        while q:
            u = q.popleft()
            for v in graph[u]:
                degree[v]-=1
                if degree[v]==1 and coins[v]==0:
                    q.append(v)
            
            degree[u] = 0
        
        #remove 2 layers of leaves because we can grab coins from 2 layers away
        q = deque()
        for i in range(n):
            if degree[i]==1:
                q.append(i)
        
        for _ in range(2):
            size = len(q)
            for _ in range(size):
                u = q.popleft()
                for v in graph[u]:
                    degree[v]-=1
                    if degree[v]==1:
                        q.append(v)
                degree[u] = 0
        
        #count remaining nodes
        remaining = sum(1 for d in degree if d>0)
        if remaining == 0:
            return 0
        
        #k nodes at the end remaining with k-1 edges twice go to them once for going and once for return
        return 2 * (remaining-1)

        
