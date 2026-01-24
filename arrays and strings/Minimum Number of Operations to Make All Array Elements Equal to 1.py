#GCD 
class Solution:
    def minOperations(self, nums: List[int]) -> int:

        n = len(nums)
        countOnes = 0
        g = 0

        for num in nums:
            if num == 1:
                countOnes+=1

            g = gcd(g, num)
        
        if countOnes>0:
            return n - countOnes
        
        if g>1:
            return -1
        
        min_len = n
        #smallest window with gcd = 1
        for i in range(n):
            g = 0
            for j in range(i, n):
                g = gcd(g, nums[j])
                if g==1:
                    min_len = min(min_len, j-i+1)
                    break
        
        #least operations to make the gcd 1 + to make rest of the elements 1
        return (min_len - 1) + (n-1)
        
        
