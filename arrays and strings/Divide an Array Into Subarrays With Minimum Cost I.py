class Solution:
    def minimumCost(self, nums: List[int]) -> int:

        n = len(nums)

        rightMin = nums[-1]
        ans = float('inf')

        for i in range(n-2, 0, -1):
            ans = min(ans, nums[0] + nums[i] + rightMin)
            rightMin = min(rightMin, nums[i])
        
        return ans
        
