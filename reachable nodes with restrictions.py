class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        seen = [False]*n
        graph = defaultdict(list)
        
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        for node in restricted:
            seen[node] = True
        
        def dfs(node):
            seen[node] = True
            self.ans+=1
            
            for neighbor in graph[node]:
                if not seen[neighbor]:
                    dfs(neighbor)
        
        self.ans = 0
        dfs(0)
        return self.ans
