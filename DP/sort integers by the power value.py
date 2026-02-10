class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:

        power_cache = {1: 0}

        def power(x):
            if x not in power_cache:
                if x%2 == 0:
                    power_cache[x] = 1 + power(x//2)
                else:
                    power_cache[x] = 1 + power(3*x+1)
                
            return power_cache[x]
        
        nums = []
        for x in range(lo, hi+1):
            nums.append((power(x), x))
        
        nums.sort()
        return nums[k-1][1]
        
