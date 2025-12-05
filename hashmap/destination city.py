class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        outgoing = set()

        for i in range(len(paths)):
            outgoing.add(paths[i][0])
        
        for i in range(len(paths)):
            candidate = paths[i][1]
            if candidate not in outgoing:
                return candidate
        
        return ""
        