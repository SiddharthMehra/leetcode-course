class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        graph = defaultdict(list)
        
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        seen = [False]*n
        
        def dfs(node):
            if node == destination:
                return True
            if not seen[node]:
                seen[node]=True
                for next_node in graph[node]:
                    if dfs(next_node):
                        return True
            
            return False
        
        return dfs(source)
        
