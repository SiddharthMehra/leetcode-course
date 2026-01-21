class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n>=k + maxPts -1:
            return 1.0
        
        dp = [0.0] * (n+1)
        dp[0] = 1.0

        windowSum = 1.0
        result = 0.0

        for i in range(1, n+1):
            dp[i] = windowSum/maxPts

            #if sum less than k, continue to add
            if i<k:
                windowSum+=dp[i]
            
            #cannot add to window sum, just compute the result
            else:
                result+=dp[i]
            
            #slide the window
            if i-maxPts>=0:
                windowSum-=dp[i-maxPts]
        
        return result
        
