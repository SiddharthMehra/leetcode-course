class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        memo = {}
        def dfs(emp):
            if emp in memo:
                return memo[emp]
            
            if manager[emp]==-1:
                memo[emp] = informTime[emp]
            
            else:
                memo[emp] = informTime[emp] + dfs(manager[emp])
            
            return memo[emp]
        
        return max(dfs(i) for i in range(n))



        
