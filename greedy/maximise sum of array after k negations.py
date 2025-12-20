class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()

        i=0
        #make the lowest elements in the array change sign
        while i<len(nums) and i<k and nums[i]<0:
            nums[i]=-nums[i]
            i+=1
        
        #if remaining is odd, all others can be flipped twice to get the original except the min 
        if (k-i)%2==1:
            idx = nums.index(min(nums))
            nums[idx]*=-1
        
        return sum(nums)
        


