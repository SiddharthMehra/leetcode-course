class Solution:
    def numberOfSequence(self, n: int, sick: List[int]) -> int:

        MOD = 10**9+7
        sick.sort()

        segments = []

        #left segment
        if sick[0]>0:
            segments.append(sick[0])
        
        #middle segment
        for i in range(1, len(sick)):
            gap = sick[i] - sick[i-1] - 1
            if gap>0:
                segments.append(gap)
        
        #right segment
        if sick[-1]<n-1:
            segments.append(n - 1 - sick[-1])
        
        #total that cam be affected
        total = sum(segments)

        fact = [1]* (total+1)
        inv = [1]* (total+1)

        for i in range(1, total+1):
            fact[i] = fact[i-1] * i % MOD
        
        inv[total] = pow(fact[total], MOD-2, MOD)
        for i in range(total, 0, -1):
            inv[i-1] = inv[i] * i % MOD
        
        res = fact[total]
        for k in segments:
            res = res * inv[k] % MOD
        
        #count internal ways inside middle segments
        for i in range(1, len(sick)):
            gap = sick[i] - sick[i-1] - 1
            if gap>0:
                res = res * pow(2, gap-1, MOD) % MOD
    
        return res

        


        
