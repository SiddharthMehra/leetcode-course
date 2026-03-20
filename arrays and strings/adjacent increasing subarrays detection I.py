class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:

        n = len(nums)
        prev_len = 0
        curr_len = 1

        for i in range(1, n):
            if nums[i]>nums[i-1]:
                curr_len+=1
            
            else:
                prev_len = curr_len
                curr_len = 1
            
            #case 1 both segments>=k
            if prev_len>=k and curr_len>=k:
                return True
            
            #case 2: single long segment can be split into two
            if curr_len>=2*k:
                return True
        
        return False
        
