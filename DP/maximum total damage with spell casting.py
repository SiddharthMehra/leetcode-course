from collections import Counter
from typing import List

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:

        count = Counter(power)

        vals = sorted(count.keys())
        total = [v * count[v] for v in vals]

        n = len(vals)
        dp=[0]*n

        for i in range(n):

            #option 1 -> skip
            skip = dp[i-1] if i>0 else 0
            #option 2 -> take, find last index j where vals[j]<vals[i]-2
            limit = vals[i] - 2
            j = bisect.bisect_left(vals, limit) - 1

            take = total[i]
            if j>=0:
                take+=dp[j]
            
            dp[i] = max(skip, take)
        
        return dp[-1]
