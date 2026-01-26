class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        max_val = ans = current_streak = 0

        #maximum bitwise AND will be when each num in array is equal to each other and is the max number in the array
        for num in nums:
            if max_val<num:
                max_val = num
                ans = current_streak = 0
            
            if max_val == num:
                current_streak+=1
            
            else:
                current_streak = 0
            
            ans = max(ans, current_streak)
        
        return ans
