class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dp(index, curr_sum):
            if (index, curr_sum) in memo:
                return memo[(index, curr_sum)]
            
            if index == len(nums):
                return 1 if curr_sum == target else 0
            
            add = dp(index+1, curr_sum + nums[index])
            subtract = dp(index+1, curr_sum + (- nums[index]))

            memo[(index, curr_sum)] = add + subtract
            return memo[(index, curr_sum)]
    
        return dp(0, 0)


