class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:

        n = len(quiet)

        graph = [[] for _ in range(n)]
        for u,v in richer:
            graph[v].append(u)
        
        ans = [None] * n
        def dfs(node):

            if ans[node] is None:
                ans[node] = node
                for child in graph[node]:
                    cand = dfs(child)
                    if quiet[cand]<quiet[ans[node]]:
                        ans[node] = cand
            
            return ans[node]
        
        return list(map(dfs, range(n)))
        
