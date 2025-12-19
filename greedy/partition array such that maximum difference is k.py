class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 1
        initial = nums[0]
        for num in nums:
            if num - initial>k:
                #create new group
                ans+=1 
                initial = num #reset the new first element
        
        return ans



