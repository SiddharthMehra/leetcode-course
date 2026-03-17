class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:

        graph = defaultdict(list)
        indegree = [0] * n

        for (x,y) in relations:
            graph[x-1].append(y-1)
            indegree[y-1]+=1
        
        q = deque()
        max_time = [0] * n

        for node in range(n):
            if indegree[node] == 0:
                q.append(node)
                max_time[node] = time[node]
        
        while q:
            node = q.popleft()
            for neighbor in graph[node]:
                max_time[neighbor] = max(max_time[neighbor], max_time[node] + time[neighbor])
                indegree[neighbor]-=1
                if indegree[neighbor]==0:
                    q.append(neighbor)
    
        return max(max_time)
