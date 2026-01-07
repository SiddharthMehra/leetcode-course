class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        gaps = [0]*(n+1)

        gaps[0] = startTime[0]
        gaps[n] = eventTime - endTime[-1]
        for i in range(1, n):
            gaps[i] = startTime[i] - endTime[i-1]
        
        #initial sliding window with k gaps
        window = sum(gaps[:k+1])
        ans = window
        #try to fill k consecutive gaps for the maximum amount of free time
        for i in range(k+1, n+1):
            window+= gaps[i] - gaps[i-(k+1)]
            ans = max(ans, window)
        
        return ans
        
