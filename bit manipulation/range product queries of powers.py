class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        bits = []
        pos = 0
        MOD = 10**9+7
        #extract bits where n has a 1
        while n>0:
            if n & 1:
                bits.append(pos)
            n>>=1
            pos+=1
        
        prefix = [0]
        for b in bits:
            prefix.append(prefix[-1] + b)
        
        res = []
        for l, r in queries:
            exp = prefix[r+1] - prefix[l]
            res.append(pow(2, exp, MOD))
        
        return res
        

        

        
