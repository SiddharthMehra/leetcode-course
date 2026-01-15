class Solution:
    def jump(self, nums: List[int]) -> int:
        ans, n = 0, len(nums)
        curr_end, furthest = 0, 0

        for i in range(n-1):
            #farthest reachable index of this jump
            furthest = max(furthest, i + nums[i])

            #starting range of this jump finished
            if i == curr_end:
                ans+=1
                curr_end = furthest
        
        return ans

        


