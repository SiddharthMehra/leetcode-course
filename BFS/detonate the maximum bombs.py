class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        n=len(bombs)
        
        for i in range(n):
            for j in range(n):
                if i==j:
                    continue
                xi, yi, ri = bombs[i]
                xj, yj, rj = bombs[j]
                if (ri**2) >= (xi-xj)**2 + (yi-yj)**2:
                    graph[i].append(j)
        
        def bfs(i):
            q=deque([i])
            visited = set([i])
            while q:
                curr = q.popleft()
                for neighbor in graph[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)
            
            return len(visited)
        
        ans=0
        for i in range(n):
            ans = max(ans, bfs(i))
        
        return ans
                
