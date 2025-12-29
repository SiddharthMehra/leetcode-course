class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        n = len(s)
        words = set(wordDict)
        dp = [False] * (n+1)
        dp[0] = True

        #if you can break upto jth index using the words in dict and j to i also, that means you can do it till index i
        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break
        
        return dp[-1]
