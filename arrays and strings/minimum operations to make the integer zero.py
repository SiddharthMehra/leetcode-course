class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:

        for k in range(1, 61):
            #remaining = sum of powers of 2.
            remaining = num1 - k * num2

            if remaining<0:
                break
            
            #min sum of k powers is k and binary representation uses the least powers
            if remaining>=k and bin(remaining).count('1')<=k:
                return k
            
        
        return -1
