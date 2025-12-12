class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        roads = set()
        graph = defaultdict(list)

        for a,b in connections:
            graph[a].append(b)
            graph[b].append(a)
            roads.add((a,b))
        
        def dfs(node):
            ans = 0
            for neighbor in graph[node]:
                if neighbor not in seen:
                    if (node,neighbor) in roads:
                        ans+=1
                    seen.add(neighbor)
                    ans+=dfs(neighbor)
            
            return ans
        
        seen={0}
        return dfs(0)
            
