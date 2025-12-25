class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph)-1
        
        def backtrack(curr_node, path):
            if curr_node == target:
                ans.append(list(path))
                return
            
            for next_node in graph[curr_node]:
                path.append(next_node)
                backtrack(next_node, path)
                path.pop()
        
        ans = []
        #path always starts from 0
        backtrack(0, [0])
        return ans
        
