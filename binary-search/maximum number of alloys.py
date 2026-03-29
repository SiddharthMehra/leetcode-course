class Solution:
    def func(sekf, mid, budget, composition, stock, cost):

        minCost = float('inf')
        for i in range(len(composition)):
            currCost = 0

            for j in range(len(composition[i])):
                curr = mid * composition[i][j]

                if stock[j]>=curr:
                    continue
                
                else:
                    extra = (curr - stock[j]) * cost[j]
                    currCost+=extra
            
            minCost = min(currCost, minCost)
        
        return minCost<=budget
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:

        low = 0
        high = int(1e9)
        ans = 0

        while low<=high:
            mid = (low+high)//2
            if self.func(mid, budget, composition, stock, cost):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return ans
        
