class Solution:
    def maxCapacity(self, costs: List[int], capacity: List[int], budget: int) -> int:

        n = len(costs)

        items = sorted(zip(costs, capacity))

        cap_prefix = [0] * n
        for i, (_, cap) in enumerate(items):
            cap_prefix[i] = max(cap_prefix[i-1] if i>0 else 0, cap)
        
    
        result, r = 0, n-1
        for l, (cst, cap) in enumerate(items):
            if cst>=budget:
                break
        
            #one mcahine
            result = max(result, cap_prefix[l])

            #two machines
            limit = budget - cst
            while r>=0 and items[r][0]>=limit:
                r-=1
            
            #take only in range[0, i] to avoid using same machine twice
            j = min(r, l-1)

            if j>=0:
                result = max(result, cap + cap_prefix[j])
        
        return result
            

