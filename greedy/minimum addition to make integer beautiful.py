class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        n0 = n
        i=0
        #sum of digits, first map string to int then sum
        while sum(map(int, str(n)))>target:
            n = n//10+1
            i+=1
        
        #final number is n*(10**i). subtract original to get difference to be added
        return n*(10**i) - n0


