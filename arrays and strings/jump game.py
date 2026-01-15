class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #iterate from last, check if you can reach the first position

        lastPos = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            if i+nums[i]>=lastPos:
                lastPos = i
        
        return lastPos == 0
