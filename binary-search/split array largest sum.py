from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def min_subarrays_required(max_sum_allowed):
            current_sum = 0
            splits_required = 0

            for element in nums:
                if current_sum + element<=max_sum_allowed:
                    current_sum+=element
                
                else:
                    current_sum = element
                    splits_required+=1
            
            return splits_required+1
        
        left, right = max(nums), sum(nums)
        while left<=right:
            max_sum_allowed = (left+right)//2
            if min_subarrays_required(max_sum_allowed)<=k:
                right = max_sum_allowed-1
                minimum_largest_split_sum = max_sum_allowed
            
            else:
                left = max_sum_allowed+1
        
        return minimum_largest_split_sum
