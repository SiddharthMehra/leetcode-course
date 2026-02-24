class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        
        #prefix sum + binary search
        n = len(stations)

        prefix = [0] * (n+1)
        for i in range(n):
            prefix[i+1] = prefix[i]+ stations[i]
        
        power = [0] * n
        for i in range(n):
            left = max(0, i-r)
            right = min(n-1, i+r)
            power[i] = prefix[right+1] - prefix[left]
        
        low, high = 0, sum(stations) + k

        def canMake(target):
            extra = 0
            added = [0] * n
            window_sum = 0

            for i in range(n):
                if i>r:
                    window_sum-=added[i-r-1]
                
                current = power[i] + window_sum

                if current<target:
                    need = target - current
                    extra+=need
                    
                    if extra>k:
                        return False
                    
                    #add stations to the furthest right to maximise
                    pos = min(n-1, i+r)
                    added[pos]+=need
                    window_sum+=need
            
            return True
        
        while low<high:
            mid = (low+high+1)//2
            if canMake(mid):
                low = mid
            else:
                high = mid-1
        
        return low

        
