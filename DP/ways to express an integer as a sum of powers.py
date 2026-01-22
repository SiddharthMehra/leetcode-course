class Solution:
    def numberOfWays(self, n: int, x: int) -> int:

        MOD = 10**9+7

        powers = []
        i=1

        while i**x<=n:
            powers.append(i**x)
            i+=1
        
        dp = [0] * (n+1) #dp[s] = number of ways to make s
        dp[0] = 1 #one way to make sum 0, choose nothing

        #dp[s]-> use p, dp[s-p] -> do not use p
        for p in powers:
            for s in range(n, p-1, -1):
                dp[s] = (dp[s] + dp[s-p]) % MOD
        
        return dp[n]

        
