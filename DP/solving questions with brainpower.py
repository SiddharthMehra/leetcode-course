class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        memo = {}

        def dfs(i):
            if i>=n:
                return 0
            
            if i in memo:
                return memo[i]
            
            points, questionSkip = questions[i]

            skip = dfs(i+1)
            solve = points + dfs(i+questionSkip+1)

            memo[i] = max(skip, solve)
            return memo[i]
        
        return dfs(0)
            
