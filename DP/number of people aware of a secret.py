class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:

        MOD = 10**9+7

        dp = [0] * (n+1)
        #only 1 person knows the secret on the first day
        dp[1] = 1

        sharing = 0

        #after delay days, person remembers so added to the sliding window, and after forget days you forget so subtracted from the sliding window
        for day in range(2, n+1):
            if day - delay>=1:
                sharing = (sharing + dp[day-delay]) % MOD
            if day - forget>=1:
                sharing = (sharing - dp[day-forget]) % MOD
            
            dp[day] = sharing
        
        result = 0
        #only people in the last forget days remember the secret finally
        for day in range(max(1, n-forget+1), n+1):
            result = (result + dp[day]) %MOD
        
        return result
            
