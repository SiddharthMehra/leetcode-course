from collections import defaultdict

class Solution:
    def sumOfGoodSubsequences(self, nums: List[int]) -> int:

        count = Counter()
        res = Counter()
        mod = 10**9+7

        for num in nums:
            #count subsequences ending at num-1, num+1 and at num itself
            count[num]+=count[num-1] + count[num+1] + 1
            count[num]%=mod
            res[num] += res[num-1] + res[num+1] + num * (count[num-1] + count[num+1] + 1)
            res[num]%=mod
        
        return sum(res.values()) % mod

