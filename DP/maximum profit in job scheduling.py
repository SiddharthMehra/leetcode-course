class Solution:
    def jobScheduling(self, startTime, endTime, profit):
        intervals = sorted(zip(startTime, endTime, profit))
        memo = {}

        def dfs(i):
            if i == len(intervals):
                return 0
            
            if i in memo:
                return memo[i]
            
            #dont include
            res = dfs(i+1)

            #include, find the next valid interval j
            j = bisect.bisect(intervals, (intervals[i][1], -1, -1))
            #take current profit and then move to next valid interval j
            res = max(res, intervals[i][2] + dfs(j))

            memo[i] = res
            return res
        
        return dfs(0)
