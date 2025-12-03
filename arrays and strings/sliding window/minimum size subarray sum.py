class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        sumOfCurrentWindow = 0
        res = float('inf')

        for right in range(0, len(nums)):
            sumOfCurrentWindow+=nums[right]

            while sumOfCurrentWindow>=target:
                res = min(res, right-left+1) 
                sumOfCurrentWindow-=nums[left] #try to find a smaller window
                left+=1
        
        return res if res!=float('inf') else 0
            





     