#sort

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        content_children = 0
        idx = 0
        g.sort()
        s.sort()
        while idx<len(s) and content_children<len(g):
            if s[idx]>=g[content_children]:
                content_children+=1
            idx+=1
        return content_children

        
