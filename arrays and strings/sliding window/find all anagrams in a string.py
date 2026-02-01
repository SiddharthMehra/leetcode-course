class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        if len(p)>len(s):
            return []
        
        pcount, scount = defaultdict(int), defaultdict(int)
        for i in range(len(p)):
            pcount[p[i]]+=1
            scount[s[i]]+=1
        
        res = [0] if scount == pcount else []
        l=0

        for r in range(len(p), len(s)):
            scount[s[r]]+=1
            scount[s[l]]-=1

            if scount[s[l]] == 0:
                scount.pop(s[l])
            
            l+=1

            if scount == pcount:
                res.append(l)
            
        
        return res


