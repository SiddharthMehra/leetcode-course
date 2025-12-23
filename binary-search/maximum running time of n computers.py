class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        left, right = 1, sum(batteries)//n
        while left<right:
            mid = (left+right+1)//2

            charge = 0
            for battery in batteries:
                #run for atmost mid minutes
                charge+=min(battery, mid)
            
            #each battery contributes mid atleast, means try for larger
            if charge>=n * mid:
                left = mid
            else:
                right = mid-1
        
        return left
