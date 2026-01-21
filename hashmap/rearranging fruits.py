from collections import Counter
from typing import List

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:

        n = len(basket1)
        count = Counter(basket1) + Counter(basket2)

        #no value can be odd, wont be able to distribute between the two baskets
        for v in count.values():
            if v%2!=0:
                return -1
        
        c1 = Counter(basket1)
        c2 = Counter(basket2)

        excess1, excess2 = [], []

        for fruit in count:
            target = count[fruit]//2
            if c1[fruit]>=target:
                excess1 += [fruit] * (c1[fruit] - target)
            if c2[fruit]>=target:
                excess2+= [fruit] * (c2[fruit] - target)
        
        if not excess1:
            return 0
        
        #try to pair smallest in excess1 with largest in excess2
        excess1.sort()
        excess2.sort(reverse = True)

        min_fruit = min(basket1 + basket2)

        total_cost = 0

        #either swap basket1 with min_fruit in basket 2 or vice versa OR just swap a and b
        for a,b in zip(excess1, excess2):
            total_cost+=min(2 * min_fruit, min(a, b))
        
        return total_cost
