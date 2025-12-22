class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def canReach(mid):
            ans = 0
            for num in nums:
                ans+=math.ceil(num/mid)
            
            return ans<=threshold
        
        left, right = 1, 10**7+1
        
        while left<right:
            mid = (left+right)//2
            if canReach(mid):
                right = mid
            else:
                left = mid+1
        
        return left
        
