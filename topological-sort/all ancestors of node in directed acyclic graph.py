class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        ans = [set() for _ in range(n)]
        in_degree = [0]*n
        parent_to_kids = defaultdict(set)

        for parent, kid in edges:
            ans[kid].add(parent)
            parent_to_kids[parent].add(kid)
            in_degree[kid]+=1
        
        dq = deque([edge for edge, degree in enumerate(in_degree) if degree == 0])

        while dq:
            parent = dq.popleft() # degree 0, hence parents
            for kid in parent_to_kids[parent]:
                ans[kid].update(ans[parent])
                in_degree[kid]-=1
                if in_degree[kid] == 0:
                    dq.append(kid)
        
        return [sorted(s) for s in ans]
