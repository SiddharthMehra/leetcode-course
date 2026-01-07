class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for u,v in edges:
            graph[u].append((v, 1))
            graph[v].append((u, 0))
        
        ans = [0]*n

        #u is the parent of v for directed graph from u -> v. calcilate initial answer with 0 as root
        def dfs(u, parent = -1):
            for v,d in graph[u]:
                if v == parent:
                    continue
                #if d == 0 => edge is from v to u, so needs to be reversed
                ans[0]+=1 if d==0 else 0
                #propagate downwards
                dfs(v, u)
        
        dfs(0)

        #dfs to calculate answers with other nodes as root
        def dfs2(u, parent=-1):
            for v,d in graph[u]:
                if v == parent:
                    continue
                #original edge is u->v. if v is conceptually the root. we need to reverse direction
                if d == 1:
                    ans[v] = ans[u]+1
                #original edge is already v-> u which was already reversed earlier. so subtract it now
                else:
                    ans[v] = ans[u]-1
                
                dfs2(v, u)
        
        dfs2(0)
        return ans
