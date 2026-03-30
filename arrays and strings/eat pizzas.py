class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:

        pizzas.sort()
        n = len(pizzas)
        days = n//4

        odd_days = (days+1)//2
        even_days = days//2

        i = n-1
        res = 0

        #odd days -> take largest
        for _ in range(odd_days):
            res+=pizzas[i]
            i-=1
        
        #even days -> take second largest
        for _ in range(even_days):
            #skip largest
            i-=1
            res+=pizzas[i]
            i-=1
        
        return res
        
