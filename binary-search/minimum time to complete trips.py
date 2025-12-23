class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:

        left, right = 1, max(time)*totalTrips

        def timeEnough(mid):
            actual_trips = 0
            for t in time:
                actual_trips+=mid//t

            return actual_trips>=totalTrips

        while left<right:
            mid = (left+right)//2
            if timeEnough(mid):
                right = mid
            else:
                left = mid+1

        return left   
