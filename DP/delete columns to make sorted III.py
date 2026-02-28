class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:

        n = len(strs[0])

        memo = [-1] * n

        def dfs(i):
            if memo[i]!=-1:
                return memo[i]
            
            ans = 1

            for j in range(i+1, n):
                if all(row[i]<=row[j] for row in strs):
                    ans = max(ans, 1 + dfs(j))
            
            memo[i] = ans
            return ans
        
        longest = 0
        for i in range(n):
            longest = max(longest, dfs(i))
        
        return n-longest
