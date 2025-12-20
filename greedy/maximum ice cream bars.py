class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        n, icecream = len(costs), 0
        m = max(costs)

        costFrequency = [0]*(m+1)
        for cost in costs:
            costFrequency[cost]+=1
        
        for cost in range(1, m+1):
            if not costFrequency[cost]:
                continue
            
            if coins<cost:
                break
            
            count = min(costFrequency[cost], coins//cost)
            coins -=cost*count
            icecream+=count
        
        return icecream


