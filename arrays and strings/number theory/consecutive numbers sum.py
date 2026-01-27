class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        count = 0 
        d = 1

        #number of ways to express = number of odd divisors of n
        while d*d<=n:
            if n%d == 0:
                if d%2==1:
                    count+=1
                
                if d!=n//d and (n//d) % 2 == 1:
                    count+=1
            
            d+=1
        
        return count
