class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def answer_query(start, end):
            if start not in graph:
                return -1
            
            seen = {start}
            stack = [(start, 1)]

            while stack:
                node, ratio = stack.pop()
                if node == end:
                    return ratio
                
                for neighbor in graph[node]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        stack.append((neighbor, ratio*graph[node][neighbor]))
            
            return -1
        
        graph = defaultdict(dict)
        for i in range(len(equations)):
            num, denom = equations[i]
            graph[num][denom] = values[i]
            graph[denom][num] = 1/values[i]
        
        ans = []
        for num, denom in queries:
            ans.append(answer_query(num, denom))
        
        return ans


        
