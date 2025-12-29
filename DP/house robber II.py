class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0 or nums is None:
            return 0
        
        if len(nums)==1:
            return nums[0]
        
        def house_robber(nums):
            prev, curr = 0, 0
            for num in nums:
                temp = curr
                curr = max(num + prev, curr)
                prev = temp
            
            return curr
        
        #either exclude the first OR exclude the last since they are in a circle
        return max(house_robber(nums[1:]), house_robber(nums[:-1]))
