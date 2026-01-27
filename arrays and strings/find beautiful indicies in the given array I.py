class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        
        #KMP
        def build_lps(p):
            lps = [0] * len(p)
            j = 0
            for i in range(1, len(p)):
                while j>0 and p[i]!=p[j]:
                    j = lps[j-1]
                
                if p[i] == p[j]:
                    j+=1
                
                lps[i] = j
            
            return lps
        
        la, lb = len(a), len(b)

        #find positions of a
        pa = a + '#' + s
        lps_a = build_lps(pa)
        pos_a = [i - 2*la for i in range(len(pa)) if lps_a[i] == la]

        #find positions of b
        pb = b + '#' + s
        lps_b = build_lps(pb)
        pos_b = [i - 2*lb for i in range(len(pb)) if lps_b[i] == lb]

        #check distance condition
        res = []
        j = 0
        
        for i in pos_a:
            while j<len(pos_b) and pos_b[j]<i-k:
                j+=1
            
            if j<len(pos_b) and pos_b[j]<=i+k:
                res.append(i)
        
        return res


        
