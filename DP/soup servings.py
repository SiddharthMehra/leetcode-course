class Solution:
    def soupServings(self, n: int) -> float:
        #if n is sufficiently large, almost always 'A' will finish first
        if n>=4800:
            return 1.0
        
        #map 25 -> 1, 50 -> 2, 75 -> 3, 100 -> 4
        n = math.ceil(n/25)
        memo = {}

        def dp(a, b):
            if (a,b) in memo:
                return memo[(a, b)]
            
            #both finish at the same time
            if a<=0 and b<=0:
                return 0.5
            
            #a finishes first
            if a<=0:
                return 1.0
            
            if b<=0:
                return 0.0
            
            res = 0.25 * (
                dp(a-4, b) +
                dp(a-3, b-1) +
                dp(a-2, b-2) +
                dp(a-1, b-3)
            )

            memo[(a,b)] = res
            return res
        
        return dp(n, n)
