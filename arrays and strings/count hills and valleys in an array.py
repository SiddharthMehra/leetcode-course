class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        #if less than 3, not possible

        if len(nums)<3:
            return 0
        
        previous = nums[0]
        turning_points = 0

        for i in range(1, len(nums)-1):
            current = nums[i]
            next_value = nums[i+1]

            #no direction change
            if current == next_value:
                continue
            
            is_peak = previous<current>next_value
            is_valley = previous > current < next_value
            
            if is_peak or is_valley:
                turning_points+=1
            
            previous = current
        
        return turning_points
            
