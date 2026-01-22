class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total_drunk, empty = 0, 0

        while numBottles>0:
            total_drunk+=numBottles
            empty+=numBottles

            numBottles = empty//numExchange
            empty = empty % numExchange
        
        return total_drunk
        
