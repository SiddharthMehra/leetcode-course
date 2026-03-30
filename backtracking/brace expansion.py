class Solution:
    #backtracking
    def expand(self, s: str) -> List[str]:

        parts = []
        i=0
        n = len(s)

        #step1 -> parse string

        while i<n:
            if s[i] == '{':
                j = i
                while s[j]!='}':
                    j+=1
                
                options = s[i+1: j].split(',')
                parts.append(sorted(options))
                i=j+1
            
            else:
                parts.append(s[i])
                i+=1
        
        #step2 -> backtracking
        res = []

        def dfs(idx, path):
            if idx == len(parts):
                res.append("".join(path))
                return
            
            for ch in parts[idx]:
                path.append(ch)
                dfs(idx+1, path)
                path.pop()
        
        dfs(0, [])
        return res
        
