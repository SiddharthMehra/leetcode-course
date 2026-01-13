class Solution:
    def minOperations(self, n: int) -> int:

        powers = [1<<i for i in range(int(log2(n)) + 2)]
        operations = 0

        #greedily subtract the largest power of 2 possible from n
        while n:
            closest = powers[0]
            min_dist = abs(n-closest)

            for p in powers:
                dist = abs(n-p)
                if dist<min_dist:
                    min_dist = dist
                    closest = p
            
            n = abs(n-closest)
            operations+=1
        
        return operations
        
