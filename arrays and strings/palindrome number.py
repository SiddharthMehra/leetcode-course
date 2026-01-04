class Solution:
    def isPalindrome(self, x: int) -> bool:

        #reverses only half the digits, checks with the remaining half.
        #stops when reverse half is greater than equal to remaining to avoid overflow

        if x<0 or (x%10==0 and x!=0):
            return False
        
        revertedNumber = 0
        while x>revertedNumber:
            revertedNumber = revertedNumber*10 + x%10
            x//=10
        
        #checking revertedNumber//10 for odd length numbers middle digit does not matter
        return x==revertedNumber or x == revertedNumber // 10
