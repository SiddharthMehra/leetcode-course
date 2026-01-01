class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # find insert position using binary search and then insert

        if not intervals:
            return [newInterval]
        
        n = len(intervals)
        target = newInterval[0]
        left, right = 0, n-1

        while left<=right:
            mid = (left+right)//2
            if intervals[mid][0]<target:
                left = mid+1
            else:
                right = mid-1
        
        intervals.insert(left, newInterval)

        def mergeIntervals():
            merged = []
            for interval in intervals:
                if not merged or merged[-1][1]<interval[0]:
                    merged.append(interval)
                else:
                    merged[-1][1] = max(merged[-1][1], interval[1])
        
            return merged

        return mergeIntervals()
